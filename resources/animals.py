import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

animal = Blueprint('animals', 'animal')


@animal.route('/', methods=['GET'])
def get_all_animals():
    # return "Hello World"
    animals = [model_to_dict(animal) for animal in models.Animal.select()]
    print(animals)
    return jsonify(data = animals, status = {"code": 200, "msg": "OK"})

@animal.route('/', methods=["POST"])
def add_animal():
    payload = request.get_json()
    animal = models.Animal.create(**payload)
    print(animal.__dict__)
    animal_dict = model_to_dict(animal)
    return jsonify(data = animal_dict, status = {"code": 200, "msg": "OK"})

