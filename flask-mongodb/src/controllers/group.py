import time
from flask import Blueprint, jsonify, request
from services.cache import simple_cache
#from app import cache 

group_bp = Blueprint('group_bp', __name__)

@group_bp.route('/groups')
@simple_cache.cache.cached(timeout=60) 
def _list():
    time.sleep(5)
    data = {
        'message': 'Data obtained from the database or external service',
        'timestamp':  time.time()
    }
    print("controller:group:list:", data)
    return jsonify(data)

@group_bp.route('/groups/clean')
def _clean():
    simple_cache.delete('_list')
    return jsonify({'message': 'Data updated and cache invalidated'}), 200