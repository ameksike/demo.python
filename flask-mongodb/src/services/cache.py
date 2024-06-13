import os
from flask_caching import Cache
from redis import Redis

class RedisCache:
    def __init__(self, app=None):
        self.cache = Cache(config={
            'CACHE_TYPE': 'redis', 
            'CACHE_REDIS_URL': os.getenv('CACHE_REDIS_URL')
        })
        if app is not None:
            self.init(app)
    
    def init(self, app):
        self.cache.init_app(app)
    
    def delete(self, key):
        self.cache.delete(key)

class SimpleCache:
    def __init__(self, app=None):
        self.cache = Cache()
        if app is not None:
            self.init(app)
    
    def init(self, app):
        app.config['CACHE_TYPE'] = 'simple'
        self.cache.init_app(app)

    def delete(self, key):
        self.cache.delete(key)

simple_cache = SimpleCache()
redis_cache = RedisCache()