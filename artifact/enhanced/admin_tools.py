"""
admin_tools.py

Admin-only workflow for maintaining the Grazioso Salvare MongoDB collection.

CS 499 – Milestone Four (Databases)

Why this exists:
- The Dash dashboard is intentionally READ-ONLY.
- All write operations (create/update/delete) are isolated to this script.
- This demonstrates secure database access, least privilege, and separation of concerns.

Usage examples:
    python admin_tools.py --ping
    python admin_tools.py --count
    python admin_tools.py --create '{"name":"Test Dog","animal_type":"Dog"}'
    python admin_tools.py --update '{"name":"Test Dog"}' '{"breed":"Mixed"}'
    python admin_tools.py --delete '{"name":"Test Dog"}'

Environment variables (recommended):
    MONGO_URI
    or
    MONGO_HOST, MONGO_PORT
"""

# In a production system, this script would be executed
# using database credentials with elevated privileges.


from __future__ import annotations

import argparse
import json
import os
from typing import Any, Dict

from crud_module_enhanced import CRUD


def parse_json(value: str) -> Dict[str, Any]:
    """Parse and validate JSON input from the command line."""
    try:
        obj = json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}") from exc

    if not isinstance(obj, dict):
        raise SystemExit("JSON must be an object (dictionary).")

    return obj


def get_db() -> CRUD:
    """Create a CRUD instance using environment variables or localhost defaults."""
    mongo_uri = os.getenv("MONGO_URI")

    if mongo_uri:
        return CRUD(uri=mongo_uri, db_name="aac", collection="animals")

    return CRUD(
        host=os.getenv("MONGO_HOST", "localhost"),
        port=int(os.getenv("MONGO_PORT", "27017")),
        db_name="aac",
        collection="animals",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Admin database tools (write access)")
    parser.add_argument("--ping", action="store_true", help="Test database connectivity")
    parser.add_argument("--count", action="store_true", help="Count all documents")
    parser.add_argument("--create", type=str, help="Insert a document (JSON)")
    parser.add_argument("--update", nargs=2, metavar=("QUERY_JSON", "UPDATE_JSON"))
    parser.add_argument("--delete", type=str, help="Delete documents matching JSON query")

    args = parser.parse_args()
    db = get_db()

    if args.ping:
        try:
            db.read({}, limit=1)
            print("MongoDB connection: OK")
        except Exception as exc:
            print("MongoDB connection failed:", exc)

    if args.count:
        records = db.read({}, projection={"_id": 0})
        print("Document count:", len(records))

    if args.create:
        document = parse_json(args.create)
        inserted_id = db.create(document)
        print("Inserted document ID:", inserted_id)

    if args.update:
        query = parse_json(args.update[0])
        update_doc = parse_json(args.update[1])
        matched, modified = db.update(query, update_doc)
        print(f"Matched: {matched}, Modified: {modified}")

    if args.delete:
        query = parse_json(args.delete)
        deleted = db.delete(query, many=True)
        print("Deleted documents:", deleted)

    db.close()


if __name__ == "__main__":
    main()
