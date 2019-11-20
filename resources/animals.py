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

@animal.route('/<id>', methods=["DELETE"])
def adopt_animal(id):
    query = models.Animal.delete().where(models.Animal.id == id)
    query.execute()
    return jsonify(data = "Animal was adopted!!", status = {"code": 200, "msg": "OK"})

@animal.route('/<id>', methods=["GET"])
def display_one_animal(id):
    animal = models.Animal.get_by_id(id)
    return jsonify(data = model_to_dict(animal), status = {"code": 200, "msg": "OK"})

@animal.route('/<id>', methods=["PUT"])
def update_animal(id):
    payload = request.get_json()
    query = models.Animal.update(**payload).where(models.Animal.id == id)
    query.execute()
    animal = models.Animal.get_by_id(id)
    animal_dict = model_to_dict(animal)
    return jsonify(data = animal_dict, status = {"code": 200, "msg": "OK"})

