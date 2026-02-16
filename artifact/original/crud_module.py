from pymongo import MongoClient

class CRUD:
    def __init__(self, host="localhost", port=27017, db_name="aac", collection="animals"):
        self.client = MongoClient(f"mongodb://{host}:{port}")
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def read_query(self, query):
        return list(self.collection.find(query))

    def read(self, query):
        return self.read_query(query)
