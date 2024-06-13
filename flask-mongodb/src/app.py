from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def getDb(name="animal", database="storage"):
    client = MongoClient(
        host='host_mongodb',
        port=27017, 
        username='root', 
        password='pass',
        authSource="admin"
    )
    return client[database]

@app.route('/')
def ping_server():
    return "Welcome to Flask API."

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = getDb()
        _animals = db.animal.find()

        animals = [{
            "id": animal["id"], 
            "name": animal["name"], 
            "type": animal["type"]
        } for animal in _animals]

        return jsonify({"data": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)