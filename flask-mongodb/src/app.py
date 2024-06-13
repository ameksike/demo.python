import os
from flask import Flask
from controllers.animal import animal_bp
from controllers.group import group_bp
from services.cache import simple_cache, redis_cache

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__)
simple_cache.init(app)
redis_cache.init(app)

app.register_blueprint(animal_bp, url_prefix='/api')
app.register_blueprint(group_bp, url_prefix='/api')

@app.route('/')
def home():
    return 'FASK_API', 200

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)