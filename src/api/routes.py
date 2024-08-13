"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_current_user, JWTManager, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)
# Allow CORS requests to this API
CORS(api)


@api.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@api.route("/hello", methods=["GET"])
@jwt_required()
def get_hello():
    username = get_jwt_identity()
    dictionary = {
        "message": "hello " + username
    }
    return jsonify(dictionary)
# @api.route("/log-in", methods = ["POST"])
# def handle_log_in():
#     body = request.json
#     email = body.get("email")
#     password = body.get("password")
#     if email is None or password is None:
#         return jsonify({
#             "message": "check your body includes email & password"
#         })
#     user = User.query.filter_by(email = email).one_or_none()
#     if user is None:
#         return jsonify({
#             "message": "no such user"
#         })
    
#     if password != user.password:
#         return jsonify({
#             "message": "bad credentials, who are you?"
#         }), 400
    
#     token = create_access_token(identity=user.id)
#     return jsonify({
#         "token": token
#     }), 200

# @api.route("/very-important-private-data", methods=["GET"])
# @jwt_required()
# def handle_super_private_endpoint():
#     user = get_current_user()
#     user = User.query.get(user_id)
#     return jsonify({
#         "very-private-data": user.email
#     }), 200



