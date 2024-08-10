"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_acces_token, jwt_required, get_current_user

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route("/log-in", methods = ["POST"])
def handle_log_in():
    body = request.json
    email = body.get("email")
    password = body.get("password")
    if email is None or password is None:
        return jsonify({
            "message": "check your body includes email & password"
        })
    user = User.query.filter_by(email = email).one_or_none()
    if user is None:
        return jsonify({
            "message": "no such user"
        })
    
    if password != user.password:
        return jsonify({
            "message": "bad credentials, who are you?"
        }), 400
    
    token = create_acces_token(identity=user.id)
    return jsonify({
        "token": token
    }), 200

@api.route("/very-important-private-data", methods=["GET"])
@jwt_required()
def handle_super_private_endpoint():
    user = get_current_user()
    user = User.query.get(user_id)
    return jsonify({
        "very-private-data": user.email
    }), 200

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
