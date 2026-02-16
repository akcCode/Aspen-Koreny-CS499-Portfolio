"""
crud_module_enhanced.py

Grazioso Salvare (CS-340) – Enhanced Database Layer for CS-499

Milestone Two (Software Design & Engineering) improvements:
- Supports authenticated and unauthenticated MongoDB connections via URI or host/port (+ optional username/password).
- Adds full CRUD methods (create/read/update/delete) with consistent return shapes.
- Validates inputs early and raises clear exceptions (improves reliability and debuggability).
- Uses type hints + docstrings for maintainability.
- Centralizes connection construction so the dashboard/app layer does not handle connection details.

Milestone Three (Algorithms & Data Structures) improvements:
- Adds MongoDB aggregation support to move computation closer to the data.
- Implements a top-breeds aggregation pipeline (group/count/sort/limit) used by the dashboard.

Milestone Four (Databases) improvements:
- Implements least-privilege controls (read-only mode for the dashboard; write operations reserved for admin workflows).
- Centralizes configuration loading from environment variables to avoid hardcoding connection details.
- Adds safer defaults for destructive operations (prevents accidental delete-all without an explicit opt-in).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
import logging
import os

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError


logger = logging.getLogger(__name__)
JsonDict = Dict[str, Any]


@dataclass(frozen=True)
class MongoConfig:
    """Configuration for connecting to MongoDB."""
    host: str = "localhost"
    port: int = 27017
    db_name: str = "aac"
    collection: str = "animals"
    username: Optional[str] = None
    password: Optional[str] = None
    uri: Optional[str] = None  # if provided, overrides host/port/credentials

    # Connection tuning (safe defaults for small projects)
    server_selection_timeout_ms: int = 5000

    def build_uri(self) -> str:
        """Build a MongoDB URI. If self.uri is provided, return it unchanged."""
        if self.uri:
            return self.uri

        if self.username and self.password:
            return f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"

        return f"mongodb://{self.host}:{self.port}"

    @staticmethod
    def _env(key: str) -> Optional[str]:
        value = os.getenv(key)
        return value if value not in (None, "") else None

    @classmethod
    def from_env(cls, *, prefix: str = "MONGO", **overrides: Any) -> "MongoConfig":
        """
        Build a MongoConfig from environment variables.

        Supported variables (with default prefix 'MONGO'):
            MONGO_URI
            MONGO_HOST
            MONGO_PORT
            MONGO_DB_NAME
            MONGO_COLLECTION
            MONGO_USERNAME
            MONGO_PASSWORD

        You can override any field via keyword args (e.g., db_name="aac").
        """
        uri = cls._env(f"{prefix}_URI")
        host = cls._env(f"{prefix}_HOST") or "localhost"
        port_raw = cls._env(f"{prefix}_PORT")
        db_name = cls._env(f"{prefix}_DB_NAME") or "aac"
        collection = cls._env(f"{prefix}_COLLECTION") or "animals"
        username = cls._env(f"{prefix}_USERNAME")
        password = cls._env(f"{prefix}_PASSWORD")

        port = 27017
        if port_raw is not None:
            try:
                port = int(port_raw)
            except ValueError:
                raise ValueError(f"{prefix}_PORT must be an integer, got: {port_raw!r}")

        base = cls(
            host=host,
            port=port,
            db_name=db_name,
            collection=collection,
            username=username,
            password=password,
            uri=uri,
        )

        return cls(**{**base.__dict__, **overrides})


class CRUD:
    """
    CRUD + Aggregation data access layer for the Grazioso Salvare dashboard.

    Database enhancement focus (Milestone Four):
    - The dashboard should run in read-only mode (least privilege).
    - Write operations (create/update/delete) remain available for admin-only workflows.
    """

    def __init__(
        self,
        config: Optional[MongoConfig] = None,
        *,
        read_only: bool = False,
        allow_delete_all: bool = False,
        **kwargs: Any,
    ) -> None:
        if config is None:
            config = MongoConfig(**kwargs)  # type: ignore[arg-type]

        self._config = config
        self._read_only = bool(read_only)
        self._allow_delete_all = bool(allow_delete_all)

        self._client: MongoClient = MongoClient(
            self._config.build_uri(),
            serverSelectionTimeoutMS=self._config.server_selection_timeout_ms,
        )
        self._db: Database = self._client[self._config.db_name]
        self._collection: Collection = self._db[self._config.collection]

    @classmethod
    def from_env(
        cls,
        *,
        prefix: str = "MONGO",
        read_only: bool = False,
        allow_delete_all: bool = False,
        **overrides: Any,
    ) -> "CRUD":
        cfg = MongoConfig.from_env(prefix=prefix, **overrides)
        return cls(cfg, read_only=read_only, allow_delete_all=allow_delete_all)

    @property
    def collection(self) -> Collection:
        return self._collection

    @property
    def read_only(self) -> bool:
        return self._read_only

    def ping(self) -> bool:
        try:
            self._client.admin.command("ping")
            return True
        except Exception:
            return False

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "CRUD":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    @staticmethod
    def _require_dict(value: Any, name: str) -> JsonDict:
        if not isinstance(value, dict):
            raise TypeError(f"{name} must be a dict, got {type(value).__name__}")
        return value

    @staticmethod
    def _require_list(value: Any, name: str) -> List[Any]:
        if not isinstance(value, list):
            raise TypeError(f"{name} must be a list, got {type(value).__name__}")
        return value

    @staticmethod
    def _require_positive_int(value: Any, name: str) -> int:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
        return value

    def _require_writable(self) -> None:
        if self._read_only:
            raise PermissionError(
                "Write operation blocked: CRUD is running in read-only mode. "
                "Use an admin-only workflow with read_only=False."
            )

    def create(self, document: JsonDict) -> str:
        self._require_writable()
        document = self._require_dict(document, "document")
        try:
            result = self._collection.insert_one(document)
            return str(result.inserted_id)
        except PyMongoError as exc:
            logger.exception("MongoDB create failed")
            raise RuntimeError("MongoDB create operation failed") from exc

    def read(self, query: JsonDict, projection: Optional[JsonDict] = None, limit: int = 0) -> List[JsonDict]:
        query = self._require_dict(query, "query")
        if projection is not None:
            projection = self._require_dict(projection, "projection")
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("limit must be a non-negative integer")

        try:
            cursor = self._collection.find(query, projection)
            if limit:
                cursor = cursor.limit(limit)
            return list(cursor)
        except PyMongoError as exc:
            logger.exception("MongoDB read failed")
            raise RuntimeError("MongoDB read operation failed") from exc

    def update(self, query: JsonDict, update_doc: JsonDict, *, upsert: bool = False) -> Tuple[int, int]:
        self._require_writable()
        query = self._require_dict(query, "query")
        update_doc = self._require_dict(update_doc, "update_doc")

        if not any(k.startswith("$") for k in update_doc.keys()):
            update_doc = {"$set": update_doc}

        try:
            result = self._collection.update_many(query, update_doc, upsert=upsert)
            return int(result.matched_count), int(result.modified_count)
        except PyMongoError as exc:
            logger.exception("MongoDB update failed")
            raise RuntimeError("MongoDB update operation failed") from exc

    def delete(self, query: JsonDict, *, many: bool = True) -> int:
        self._require_writable()
        query = self._require_dict(query, "query")

        if query == {} and not self._allow_delete_all:
            raise ValueError(
                "Refusing to delete all documents with an empty query {}. "
                "Set allow_delete_all=True for explicit admin delete-all operations."
            )

        try:
            if many:
                result = self._collection.delete_many(query)
            else:
                result = self._collection.delete_one(query)
            return int(result.deleted_count)
        except PyMongoError as exc:
            logger.exception("MongoDB delete failed")
            raise RuntimeError("MongoDB delete operation failed") from exc

    def aggregate(self, pipeline: List[JsonDict]) -> List[JsonDict]:
        pipeline = self._require_list(pipeline, "pipeline")
        for i, stage in enumerate(pipeline):
            if not isinstance(stage, dict) or len(stage) != 1:
                raise ValueError(f"pipeline stage {i} must be a single-key dict like {{'$match': ...}}")

        try:
            return list(self._collection.aggregate(pipeline))
        except PyMongoError as exc:
            logger.exception("MongoDB aggregate failed")
            raise RuntimeError("MongoDB aggregate operation failed") from exc

    def top_breeds(
        self,
        *,
        match_query: Optional[JsonDict] = None,
        limit: int = 10,
        include_unknown: bool = False,
    ) -> List[JsonDict]:
        limit = self._require_positive_int(limit, "limit")
        if match_query is not None:
            match_query = self._require_dict(match_query, "match_query")

        pipeline: List[JsonDict] = []

        if match_query:
            pipeline.append({"$match": match_query})

        if not include_unknown:
            pipeline.append({"$match": {"breed": {"$nin": [None, ""]}}})

        pipeline.extend([
            {"$group": {"_id": "$breed", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": limit},
            {"$project": {"_id": 0, "breed": "$_id", "count": 1}},
        ])

        return self.aggregate(pipeline)
