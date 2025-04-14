from flask import Blueprint, request, jsonify
from src.models.role_model import Role
from src.models.permission_model import Permission
from src.db import db

role_bp = Blueprint('role_bp', __name__)

@role_bp.route('/', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    return jsonify([role.to_dict() for role in roles])

@role_bp.route('/', methods=['POST'])
def create_role():
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'message': 'Falta el nombre del rol'}), 400

    new_role = Role(name=data['name'])

    try:
        db.session.add(new_role)
        db.session.commit()
        return jsonify({
            "message": "Rol creado",
            "role": new_role.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error', 'error': str(e)}), 500

@role_bp.route('/<int:role_id>/permissions', methods=['POST'])
def assign_permissions_to_role(role_id):
    data = request.get_json()
    permission_ids = data.get('permission_ids', [])

    role = Role.query.get(role_id)
    if not role:
        return jsonify({'message': 'Rol no encontrado'}), 404

    permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()
    role.permissions = permissions

    try:
        db.session.commit()
        return jsonify({
            'message': 'Permisos asignados correctamente',
            'role': role.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al asignar permisos', 'error': str(e)}), 500

@role_bp.route('/<int:role_id>/permissions', methods=['GET'])
def get_role_permissions(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'message': 'Rol no encontrado'}), 404

    return jsonify([perm.to_dict() for perm in role.permissions])
