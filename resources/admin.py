import models
from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

admin = Blueprint('admins', 'admin')

@admin.route('/register', methods=["POST"])
def admin_register():
    payload = request.get_json()
    payload['email'].lower()
    payload['password'] = generate_password_hash(payload['password'])
    admin = models.Admin.create(**payload)
    admin_dict = model_to_dict(admin)
    return jsonify(data = admin_dict, status = {"code": 200, "msg": "OK"})

@admin.route('/login', methods=["POST"])
def login_admin():
    payload = request.get_json()
    admin = models.Admin.get(models.Admin.email == payload['email'])
    admin_dict = model_to_dict(admin)
    if check_password_hash(admin_dict['password'], payload['password']):
        login_user(admin)
        del admin_dict['password']
        return jsonify(data = admin_dict, status = {"code": 200, "msg": "OK"})
    else:
        return jsonify(data = {}, status= {"code": 401, "msg": "You are not authorized to do that"})
    
