import models

from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
# import admin


from playhouse.shortcuts import model_to_dict

animal = Blueprint('animals', 'animal')


# index route for all of the animals
@animal.route('/', methods=['GET'])
def get_all_animals():
    # return "Hello World"
    # turn the animal into a dict so it can be jsonified
    animals = [model_to_dict(animal, max_depth=0) for animal in models.Animal.select()]
    # what am I getting back?
    print(animals)
    return jsonify(data = animals, status = {"code": 200, "msg": "OK"})

# animal create/post route
@animal.route('/', methods=["POST"])
def add_animal():
    payload = request.get_json()
    if (payload['shelter']):
        payload['shelter'] == models.Shelter.get(id=payload['shelter'])
    else: 
        payload['shelter'] == 1
    animal = models.Animal.create(**payload)
    print(animal.__dict__)
    animal_dict = model_to_dict(animal, max_depth=0)
    return jsonify(data = animal_dict, status = {"code": 200, "msg": "OK"})

# adoption/delete route for selected animal
@animal.route('/<id>', methods=["DELETE"])
def adopt_animal(id):
    # if the id of the model matches the id in the url...
    query = models.Animal.delete().where(models.Animal.id == id)
    if current_user.is_authenticated:
    #this method should only be accessible to an admin and only once they are logged in 
    # execute the delete method
        query.execute()
        return jsonify(data = "Animal was adopted!!", status = {"code": 200, "msg": "OK"})
    else:
        return jsonify(data={}, status = {'code': 401, 'msg': "You are not authorized to do that"})

# show route for selected animal
@animal.route('/<id>', methods=["GET"])
def display_one_animal(id):
    # the id in this assignment should be the id from the url
    animal = models.Animal.get_by_id(id)
    return jsonify(data = model_to_dict(animal, max_depth=0), status = {"code": 200, "msg": "OK"})

# animal edit route
@animal.route('/<id>', methods=["PUT"])
def update_animal(id):
    payload = request.get_json()
    if (payload['shelter']):
        payload['shelter'] == models.Shelter.get(id=payload['shelter'])
    else: 
        payload['shelter'] == 1
    query = models.Animal.update(**payload).where(models.Animal.id == id)
    if current_user.is_authenticated:
        query.execute()
    # again, this is referencing the id in the url
    animal = models.Animal.get_by_id(id)
    # need to turn this data into a jsonifiable format(dict)
    animal_dict = model_to_dict(animal, max_depth=0)
    return jsonify(data = animal_dict, status = {"code": 200, "msg": "OK"})

