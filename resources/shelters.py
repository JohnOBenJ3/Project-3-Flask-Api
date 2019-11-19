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
        