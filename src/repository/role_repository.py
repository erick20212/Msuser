from src.db import db
from src.models.role_model import Role

class RoleRepository:

    def add(self, data):
        new_role = Role(**data)
        db.session.add(new_role)
        db.session.commit()
        return new_role

    def get(self, role_id):
        return Role.query.get(role_id)

    def get_by_name(self, name):
        return Role.query.filter_by(name=name).first()

    def get_all(self):
        return Role.query.all()

    def update(self, role, data):
        for key, value in data.items():
            if hasattr(role, key):
                setattr(role, key, value)
        db.session.commit()
        return role

    def delete(self, role):
        db.session.delete(role)
        db.session.commit()