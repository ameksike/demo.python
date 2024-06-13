from flask import Flask, request
from flask_restful import Api
from controllers.Animal import Animal, AnimalList

app = Flask(__name__)
api = Api(app)

api.add_resource(Animal, '/api/animals/<int:animal_id>')
api.add_resource(AnimalList, '/api/animals')


if __name__ == '__main__':
    app.run(debug=True)
