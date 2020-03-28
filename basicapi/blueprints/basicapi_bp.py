from flask import Blueprint, render_template, request, json
from ..extensions import db
from basicapi.models.user import User
from basicapi.models.data import Data
from basicapi.models.task import Task

basicapi_bp = Blueprint('basicapi_bp', __name__)


@basicapi_bp.route('/')
def index():
    users = [{'name': user.first_name} for user in User.get_all()]
    return render_template('index.html', app_name='basicAPI', users=json.dumps(users))


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


@basicapi_bp.route('/ezApi', methods=['GET', 'POST'])
def dataFunction():
    if request.method == 'GET':
        all_data = [x for x in Data.get_all()]
        all_data.sort(key=lambda x: x.id, reverse=False)
        all_data = [x.serialize for x in all_data]
        return json.dumps(all_data), 200, {'ContentType': 'application/json'}
    elif request.method == 'POST':
        try:
            all_data = Data.get_all()
            if len(all_data) > 59:
                all_data.sort(key=lambda x: x.id, reverse=False)
                db.session.delete(all_data[0])
            d = Data(
               value=float(request.args.get('value'))
            )
            db.session.add(d)
            db.session.commit()
            return '201'
        except:
            return '404'



@basicapi_bp.route('/ezApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bookFunctionId(id):
    if request.method == 'GET':
        try:
            all_data = [x.id for x in Data.get_all()]
            if id in all_data:
                matching_data = Data.get(int(id))
                return matching_data.serialize
            else:
                return '404'
        except:
            return '404'
    elif request.method == 'DELETE':
        try:
            matching_data = Data.get(int(id))
            if matching_data:
                db.session.delete(matching_data)
                db.session.commit()
                return 'Removed data id ' + str(id)
            else:
                return '304'
        except:
            return '304'


@basicapi_bp.route('/ezApi/users', methods=['GET', 'POST'])
def users_basic():
    if request.method == 'GET':
        all_data = [x for x in User.get_all()]
        all_data.sort(key=lambda x: x.id, reverse=False)
        all_data = [x.serialize for x in all_data]
        return json.dumps(all_data), 200, {'ContentType': 'application/json'}
    elif request.method == 'POST':
        try:
            all_data = [x.first_name for x in User.get_all()]
            if request.args.get('first_name') in all_data:
                return '304'
            u = User(
                first_name=request.args.get('first_name')
            )
            db.session.add(u)
            db.session.commit()
            return '201'
        except:
            return '404'


@basicapi_bp.route('/ezApi/users/<int:id>', methods=['GET', 'DELETE'])
def user_by_id(id):
    if request.method == 'GET':
        try:
            all_data = [x.id for x in User.get_all()]
            if id in all_data:
                matching_data = User.get(int(id))
                return matching_data.serialize
            else:
                return '404'
        except:
            return '404'
    elif request.method == 'DELETE':
        try:
            matching_data = User.get(int(id))
            if matching_data:
                db.session.delete(matching_data)
                db.session.commit()
                return 'Removed user id ' + str(id)
            else:
                return '304'
        except:
            return '304'