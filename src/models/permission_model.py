from src.db import db
from src.models.base_model import BaseModelMixin

class Permission(db.Model, BaseModelMixin):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    roles = db.relationship('Role', secondary='role_permissions', back_populates='permissions')
