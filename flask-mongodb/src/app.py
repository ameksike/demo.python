import os
from flask import Flask
from controllers.animal import animal_bp

"""
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
"""

def create_app():
    app = Flask(__name__)
    app.register_blueprint(animal_bp, url_prefix='/api')
    return app

if __name__=='__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)