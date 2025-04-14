# src/repository/permission_repository.py

from src.db import db
from src.models.permission_model import Permission

class PermissionRepository:

    def add(self, data):
        new_permission = Permission(**data)
        db.session.add(new_permission)
        db.session.commit()
        return new_permission

    def get(self, permission_id):
        return Permission.query.get(permission_id)

    def get_by_name(self, name):
        return Permission.query.filter_by(name=name).first()

    def get_all(self):
        return Permission.query.all()

    def update(self, permission, data):
        for key, value in data.items():
            if hasattr(permission, key):
                setattr(permission, key, value)
        db.session.commit()
        return permission

    def delete(self, permission):
        db.session.delete(permission)
        db.session.commit()
