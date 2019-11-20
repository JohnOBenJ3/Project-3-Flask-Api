import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

shelter = Blueprint('shelters', 'shelter')


@shelter.route('/', methods=['GET'])
def get_all_shelters():
    # return "Hello World"
    try:
        shelters = [model_to_dict(shelter) for shelter in models.Shelter.select()]
        print(shelters)
        return jsonify(data = shelters, status = {"code": 200, "msg": "OK"})
    except models.DoesNotExist:
        return jsonify(data = {}, status = {"code": 401, "msg": "Unauthorized"})

@shelter.route('/', methods=["POST"])
def create_shelter():
    # we want to get back the json object for manipulation from the db
    payload = request.get_json()
    # payload should have the properties we need to create the new instance
    shelter = models.Shelter.create(**payload)
    print(shelter.__dict__)
    # we need this to be a dictionary object
    shelter_dict = model_to_dict(shelter)
    # if everything in the route goes well, we should see this message along with the data 
    # being the newly created instance
    return jsonify(data = shelter_dict, status = {"code": 200, "msg": "OK"})

@shelter.route('/<id>', methods=["GET"])
def show_one_shelter(id):
    #does the id match what i think it should match?
    print(id)
    shelter = models.Shelter.get_by_id(id)
    return jsonify(data = model_to_dict(shelter), status = {"code": 200, "msg": "OK"})

@shelter.route('/<id>', methods=["PUT"])
def change_shelter_specs(id):
    payload = request.get_json()
    # if the id of the thing I am searching is == to the id in the url, execute this peewee/SQL method
    query = models.Shelter.update(**payload).where(models.Shelter.id == id)
    query.execute()
    shelter = models.Shelter.get_by_id(id)
    shelter_dict = model_to_dict(shelter)
    return jsonify(data = shelter_dict, status = {"code": 200, "msg": "OK"})

@shelter.route('/<id>', methods=["DELETE"])
def remove_shelter(id):
    # making sure that the id of the thing I get back is the same as the id in the url
    # if it is, then the peewee/SQL query/method of delete should execute when the execute method
    # is invoked 
    query = models.Shelter.delete().where(models.Shelter.id == id)
    # execute the delete query
    query.execute()
    # the instance should now be deleted and only this message should return. Check the db to make sure
    # that that particular record was indeed removed
    return jsonify(data = "Shelter was removed", status = {"code": 200, "msg": "OK"})

        