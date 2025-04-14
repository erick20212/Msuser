from flask import Blueprint, request, jsonify
from src.models.user_model import User
from src.models.role_model import Role
from src.db import db
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    if not all(key in data for key in ('email', 'password')):
        return jsonify({'message': 'Faltan datos'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(email=data['email'], password=hashed_password)

    try:
        # Primero agregar al session
        db.session.add(new_user)

        # Asignar rol 'USER' si existe
        default_role = Role.query.filter_by(name='USER').first()
        if default_role:
            new_user.roles.append(default_role)

        db.session.commit()
        return jsonify({
            "message": "Usuario creado con rol por defecto",
            "user": new_user.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error', 'error': str(e)}), 500

@user_bp.route('/<int:user_id>/roles', methods=['POST'])
def assign_roles_to_user(user_id):
    data = request.get_json()
    role_ids = data.get('role_ids', [])

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    roles = Role.query.filter(Role.id.in_(role_ids)).all()
    user.roles = roles

    try:
        db.session.commit()
        return jsonify({
            'message': 'Roles asignados correctamente',
            'user': user.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al asignar roles', 'error': str(e)}), 500

@user_bp.route('/<int:user_id>/roles', methods=['GET'])
def get_user_roles(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    return jsonify([role.to_dict() for role in user.roles])
