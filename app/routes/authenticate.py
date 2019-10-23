import datetime

import jwt
from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import check_password_hash

from app.models.user import User

authenticate = Blueprint('authenticate', __name__)

@authenticate.route('/verify/<token>', methods= ['GET'])
def verify(token):
    try:
        data = jwt.decode(token, current_app.config.get('SECRET_KEY'))
        return jsonify({'current_user': data['public_id']})
    except Exception as e:
        return jsonify({'Message': 'Invalid Token'}), 401


@authenticate.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data['username']
    password = data['password']

    user = User.query.filter_by(user_name=username).first()
    if not user:
        return jsonify({'Message': 'Invalid username or password'})

    if check_password_hash(user.password, password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            current_app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})