from flask import Blueprint, request, jsonify
from src.models.user_model import User
from werkzeug.security import check_password_hash
from src.config.config import Config
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not all(key in data for key in ('email', 'password')):
        return jsonify({'message': 'Faltan datos'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Credenciales incorrectas'}), 401

    # Generar token JWT
    token = jwt.encode({
        'sub': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, Config.SECRET_KEY, algorithm='HS256')

    return jsonify({
        'message': 'Login exitoso',
        'token': token
    }), 200
