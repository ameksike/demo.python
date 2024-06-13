from pymongo import MongoClient

def getDb(name="animal", database="storage"):
    client = MongoClient(
        host='host_mongodb',
        port=27017, 
        username='root', 
        password='pass',
        authSource="admin"
    )
    return client[database]
    
def delDb(conn):
    if type(conn)==MongoClient:
            conn.close()
        