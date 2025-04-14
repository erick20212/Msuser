from src.models.user_model import User
from src.db import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user, data):
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()
