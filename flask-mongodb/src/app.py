from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

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

@app.route('/api/animals')
def list_animals():
    db=""
    try:
        collection = getDb().animal
        res = collection.find()
        data = [{
            "id": animal["id"], 
            "name": animal["name"], 
            "type": animal["type"]
        } for animal in res]

        return jsonify({
            "size": len(data),
            "data": data
        })
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/api/animals/<int:id>', methods=['GET'])
def select_animal(id):
    try:
        # _id = ObjectId(id) 
        collection = getDb().animal
        item  = collection.find_one({'id': int(id)})
        if item:
            return jsonify({
                "id": item["id"], 
                "name": str(item["name"]), 
                "type": item["type"]
            }), 200
        else:
            return jsonify({'error': 'Item not found'}), 404
    except InvalidId as e:
        return jsonify({'error': 'Invalid ID format', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

@app.route('/api/animals', methods=['POST'])
def insert_animal():
    try:
        # _id = ObjectId(id) 
        item = request.json
        collection = getDb().animal
        result = collection.insert_one(item)
        return jsonify({'message': 'Item inserted', 'id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

@app.route('/api/animals/<id>', methods=['PUT'])
def update_item(id):
    try:
        # _id = ObjectId(id) 
        collection = getDb().animal
        item = request.json
        result = collection.update_one({'id': int(id)}, {'$set': item})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated'}), 200
        else:
            return jsonify({'error': 'Item not found or not modified'}), 404
    except InvalidId:
        return jsonify({'error': 'Invalid ID format'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

@app.route('/api/animals/<id>', methods=['DELETE'])
def delete_item(id):
    try:
        # item_id = ObjectId(id)
        collection = getDb().animal
        result = collection.delete_one({'id': int(id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Item deleted'}), 200
        else:
            return jsonify({'error': 'Item not found'}), 404
    except InvalidId:
        return jsonify({'error': 'Invalid ID format'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)