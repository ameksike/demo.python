animals = {
    1: {"name": "Lion", "species": "Panthera leo"},
    2: {"name": "Tiger", "species": "Panthera tigris"},
    3: {"name": "Elephant", "species": "Loxodonta africana"}
}
from flask_restful import Resource, reqparse

class Animal(Resource):
    def get(self, animal_id):
        animal = animals.get(animal_id)
        if animal:
            return animal
        else:
            return {"error": "Animal not found"}, 404

    def delete(self, animal_id):
        if animal_id in animals:
            del animals[animal_id]
            return {"message": "Animal deleted"}
        else:
            return {"error": "Animal not found"}, 404

    def put(self, animal_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank!")
        parser.add_argument('species', required=True, help="Species cannot be blank!")
        args = parser.parse_args()
        animals[animal_id] = {"name": args['name'], "species": args['species']}
        return animals[animal_id], 201
