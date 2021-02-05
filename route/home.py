from flask import Blueprint, jsonify
from api.model.welcome import WelcomeModel

home_api = Blueprint('api', __name__)


@home_api.route('/')
def welcome():
    if request.method == 'GET':
        return jsonify({'tasks': "teste", 'success': 1})
