import models
from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

admin = Blueprint('admins', 'admin')

@admin.route('/login', methods=["POST"])
def admin_login():
    payload = request.get_json()
    payload['email'].lower()
    payload['password'] = generate_password_hash(payload['password'])
    models.Admin.create(**payload)
    admin_dict = model_to_dict(admin)
    return jsonify(data = admin_dict, status = {"code": 200, "msg": "OK"})
