# src/service/role_service.py

from src.db import db
from src.models.role_model import Role

def get_all_roles():
    return Role.query.all()

def get_role_by_id(role_id):
    return Role.query.get(role_id)

def get_role_by_name(name):
    return Role.query.filter_by(name=name).first()

def create_role(data):
    role = Role(**data)
    db.session.add(role)
    db.session.commit()
    return role

def update_role(role, data):
    for key, value in data.items():
        setattr(role, key, value)
    db.session.commit()
    return role

def delete_role(role):
    db.session.delete(role)
    db.session.commit()
