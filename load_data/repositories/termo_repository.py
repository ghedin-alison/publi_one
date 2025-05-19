from models.class_termo import Termo
from db_connection import MongoDBConnection
from typing import Optional


class TermoRepository:
    def __init__(self):
        self.connection = MongoDBConnection()
        self.collection = self.connection.get_collection()

    def insert_one(self, termo: Termo) -> bool:
        if self.collection is not None:
            try:
                item = self.find_one({"termo": termo["termo"]})
                if item is None:
                    result = self.collection.insert_one(termo)
                    print(f"Inserted document with _id: {result.inserted_id}")
                    return True
            except Exception as e:
                print(f"Could not insert document: {e}")
                return False
        return False

    def find_all(self) -> list[Termo]:
        if self.collection is not None:
            return [Termo.from_dict(doc) for doc in self.collection.find()]
        return []

    def find_one(self, query: dict) -> Optional[Termo]:
        if self.collection is not None:
            document = self.collection.find_one(query)
            if document:
                return document
        return None

    def update_one(self, query: dict, update_data: dict) -> bool:
        if self.collection is not None:
            try:
                result = self.collection.update_one(query, {"$set": update_data})
                if result.modified_count > 0:
                    print(f"Updated document matching: {query}")
                    return True
                else:
                    print(f"No document found matching: {query}")
                    return False
            except Exception as e:
                print(f"Could not update document: {e}")
                return False
        return False

    def delete_one(self, query: dict) -> bool:
        if self.collection is not None:
            try:
                result = self.collection.delete_one(query)
                if result.deleted_count > 0:
                    print(f"Deleted document matching: {query}")
                    return True
                else:
                    print(f"No document found matching: {query}")
                    return False
            except Exception as e:
                print(f"Could not delete document: {e}")
                return False
        return False