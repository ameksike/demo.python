from pymongo import MongoClient
import os

def getDb(name="animal", database="storage_"):
    client = MongoClient(
        host=os.getenv('MONGO_INITDB_HOST'),
        port=os.getenv('MONGO_INITDB_PORT') or 27017, 
        username=os.getenv('MONGO_INITDB_ROOT_USERNAME') or 'root_', 
        password=os.getenv('MONGO_INITDB_ROOT_PASSWORD') or 'pass_',
        authSource=os.getenv('MONGO_INITDB_ADM') or "admin"
    )
    name = os.getenv('MONGO_INITDB_DATABASE') or database
    return client[name]
    
def delDb(conn):
    if type(conn)==MongoClient:
            conn.close()
        