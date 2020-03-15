from flask import Blueprint, render_template, jsonify, request, json
import string, random
from ..extensions import db
from basicapi.models.user import User

basicapi_bp = Blueprint('basicapi_bp', __name__)


@basicapi_bp.route('/')
def index():
    users = [{'name': user.first_name} for user in User.get_all()]
    return render_template('index.html', app_name='basicAPI', users=json.dumps(users))


@basicapi_bp.route('/password/<int:length>', methods=['GET'])
def generate_pass(length):
    letters_and_digits = string.ascii_letters + string.digits
    to_return = ''.join(random.choice(letters_and_digits) for i in range(length))
    return jsonify(to_return)


@basicapi_bp.route('/password/special/<int:length>', methods=['GET'])
def generate_special_pass(length):
    letters_digits_specials = string.ascii_letters + string.digits + string.punctuation
    to_return = ''.join(random.choice(letters_digits_specials) for i in range(length))
    return jsonify(to_return)


@basicapi_bp.route('/add/<first_name>', methods=['POST'])
def add_user(first_name):
    """
    Adds a user based on the vue.js input from the ajax request
    :param first_name: first name of the user
    :param email: email of the user
    :return: list of all users
    """
    u = User(
        first_name=first_name
    )
    db.session.add(u)
    db.session.commit()
    users = [{'name': user.first_name} for user in User.get_all()]
    return json.dumps(users), 200, {'ContentType': 'application/json'};
