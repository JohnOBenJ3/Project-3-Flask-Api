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

