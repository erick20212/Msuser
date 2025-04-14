# src/controller/permission_controller.py

from flask import Blueprint, request, jsonify
from src.models.permission_model import Permission
from src.db import db

permission_bp = Blueprint('permission_bp', __name__)

@permission_bp.route('/', methods=['GET'])
def get_permissions():
    permissions = Permission.query.all()
    return jsonify([p.to_dict() for p in permissions])

@permission_bp.route('/', methods=['POST'])
def create_permission():
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'message': 'Falta el nombre del permiso'}), 400

    new_permission = Permission(name=data['name'])

    try:
        db.session.add(new_permission)
        db.session.commit()
        return jsonify({
            "message": "Permiso creado",
            "permission": new_permission.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error', 'error': str(e)}), 500
