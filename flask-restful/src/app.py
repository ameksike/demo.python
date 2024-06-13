from flask import Flask, request
from flask_restful import Api
from src.controllers.Animal import Animal, AnimalList

app = Flask(__name__)
api = Api(app)

api.add_resource(Animal, '/api/animals/<int:animal_id>')
api.add_resource(AnimalList, '/api/animals')

