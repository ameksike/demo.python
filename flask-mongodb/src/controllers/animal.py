from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from bson.errors import InvalidId
from services.mongodb import getDb, delDb

animal_bp = Blueprint('animal_bp', __name__)

@animal_bp.route('/animals')
def _list():
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
        delDb(db)

@animal_bp.route('/animals/<int:id>', methods=['GET'])
def _select(id):
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

@animal_bp.route('/animals', methods=['POST'])
def _insert():
    try:
        # _id = ObjectId(id) 
        item = request.json
        collection = getDb().animal
        result = collection.insert_one(item)
        return jsonify({'message': 'Item inserted', 'id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

@animal_bp.route('/animals/<id>', methods=['PUT'])
def _update(id):
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

@animal_bp.route('/animals/<id>', methods=['DELETE'])
def _delete(id):
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
