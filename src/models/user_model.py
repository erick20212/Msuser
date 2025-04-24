from src.db import db
from src.models.base_model import BaseModelMixin
from src.models.user_roles_model import user_roles

class User(db.Model, BaseModelMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    dni = db.Column(db.String(15), unique=True, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)

    roles = db.relationship('Role', secondary=user_roles, back_populates='users')
