import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
MONGO_URI = os.getenv('MONGO_URI')


class MongoDBConnection:
    _instance = None

    def __new__(cls, uri=MONGO_URI, db_name=MONGO_DB_NAME):
        if not cls._instance:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient(uri)
                cls._instance.client.admin.command('ping')
                cls._instance.db = cls._instance.client[db_name]
                print("Connected to MongoDB (Singleton)!")
            except ConnectionFailure as e:
                print(f"Could not connect to MongoDB: {e}")
                cls._instance = None
        return cls._instance

    def get_collection(self, collection_name=MONGO_COLLECTION):
        if self.db is not None:
            return self.db[collection_name]
        return None

    def close(self):
        if self.client is not None:
            self.client.close()
            print("MongoDB connection closed.")
            MongoDBConnection._instance = None



# class MongoDBConnection:
#     _instance = None

#     def __new__(cls, uri=MONGO_URI, host=MONGO_HOST, port=MONGO_PORT, db_name=MONGO_DB):
#         if not cls._instance:
#             cls._instance = super(MongoDBConnection, cls).__new__(cls)
#             cls._instance.client = None
#             cls._instance.db = None
#             try:
#                 if uri:
#                     cls._instance.client = MongoClient(uri)
#                     print(f"Connected to MongoDB via URI (Singleton): {uri}")
#                 elif host and port:
#                     cls._instance.client = MongoClient(host, int(port))
#                     print(f"Connected to MongoDB via host and port (Singleton): {host}:{port}")
#                 else:
#                     raise ValueError("Either MONGO_URI or both MONGO_HOST and MONGO_PORT must be set.")

#                 cls._instance.client.admin.command('ping')
#                 cls._instance.db = cls._instance.client[db_name]

#             except (ConnectionFailure, ValueError) as e:
#                 print(f"Could not connect to MongoDB: {e}")
#                 cls._instance = None
#         return cls._instance

#     def get_collection(self, collection_name=MONGO_COLLECTION):
#         if self.db is not None:
#             return self.db[collection_name]
#         return None

#     def close(self):
#         if self.client is not None:
#             self.client.close()
#             print("MongoDB connection closed.")
#             MongoDBConnection._instance = None

# # Example usage (not part of the class, but shows how to use it):
# if __name__ == "__main__":
#     # Example using URI (set MONGO_URI environment variable)
#     # os.environ['MONGO_URI'] = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority"
#     db_uri = MongoDBConnection()
#     if db_uri:
#         my_collection_uri = db_uri.get_collection("my_collection")
#         if my_collection_uri:
#             print(f"Got collection: {my_collection_uri.name} (via URI)")
#         db_uri.close()

#     print("-" * 20)

#     # Example using host and port (set MONGO_HOST and MONGO_PORT environment variables)
#     # os.environ['MONGO_HOST'] = "localhost"
#     # os.environ['MONGO_PORT'] = "27017"
#     db_host_port = MongoDBConnection(uri=None) # Explicitly set uri to None to force host/port connection
#     if db_host_port:
#         my_collection_host_port = db_host_port.get_collection("another_collection")
#         if my_collection_host_port:
#             print(f"Got collection: {my_collection_host_port.name} (via host/port)")
#         db_host_port.close()

#     print("-" * 20)

#     # Example where neither URI nor host/port are set
#     del os.environ.get('MONGO_URI', None)
#     del os.environ.get('MONGO_HOST', None)
#     del os.environ.get('MONGO_PORT', None)
#     db_fail = MongoDBConnection() # This should print an error message
#     if db_fail:
#         db_fail.close()            