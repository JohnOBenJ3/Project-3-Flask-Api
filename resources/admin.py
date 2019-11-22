import models
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, login_user
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict

# admin = Blueprint('admins', 'admin')

# @admin.route('/admin/login', methods = ["POST"])
# def admin_login():
#     payload = request.get_json()
    
