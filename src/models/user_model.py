from src.db import db
from src.models.base_model import BaseModelMixin
from src.models.user_roles_model import user_roles

class User(db.Model, BaseModelMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    roles = db.relationship('Role', secondary=user_roles, back_populates='users')
