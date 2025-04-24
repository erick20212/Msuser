from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt
from sqlalchemy.exc import IntegrityError

from src.config.config import Config
from src.models.user_model import User
from src.service.user_service import register_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not all(key in data for key in ('email', 'password')):
        return jsonify({'message': 'Faltan datos'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Credenciales incorrectas'}), 401

    token = jwt.encode({
        'sub': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, Config.SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'Login exitoso', 'token': token}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    required = ('email', 'password', 'username')
    if not data or not all(k in data for k in required):
        return jsonify({'message': 'Faltan datos obligatorios'}), 400

    # Verificaciones manuales
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'El email ya está registrado'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'El nombre de usuario ya está en uso'}), 400
    if data.get('dni') and User.query.filter_by(dni=data['dni']).first():
        return jsonify({'message': 'El DNI ya está registrado'}), 400

    try:
        user = register_user(
            email=data['email'],
            password=data['password'],
            username=data['username'],
            name=data.get('name'),
            lastname=data.get('lastname'),
            dni=data.get('dni'),
            phone=data.get('phone'),
            address=data.get('address')
        )

        token = jwt.encode({
            'sub': user.id,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, Config.SECRET_KEY, algorithm='HS256')

        return jsonify({
            "message": "Usuario registrado correctamente",
            "token": token
        }), 201

    except IntegrityError as e:
        return jsonify({'message': 'Datos duplicados', 'error': str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

