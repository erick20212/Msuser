# src/service/permission_service.py

from src.db import db
from src.models.permission_model import Permission

def get_all_permissions():
    return Permission.query.all()

def get_permission_by_id(permission_id):
    return Permission.query.get(permission_id)

def get_permission_by_name(name):
    return Permission.query.filter_by(name=name).first()

def create_permission(data):
    permission = Permission(**data)
    db.session.add(permission)
    db.session.commit()
    return permission

def update_permission(permission, data):
    for key, value in data.items():
        setattr(permission, key, value)
    db.session.commit()
    return permission

def delete_permission(permission):
    db.session.delete(permission)
    db.session.commit()
