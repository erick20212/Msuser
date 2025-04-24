from werkzeug.security import generate_password_hash
from src.models.user_model import User
from src.db import db
from src.service.role_service import get_role_by_name


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

def register_user(email, password, username=None, name=None, lastname=None, dni=None, phone=None, address=None):
    if get_user_by_email(email):
        raise Exception("El correo ya está registrado")

    hashed_password = generate_password_hash(password)

    user_data = {
        "email": email,
        "password": hashed_password,
        "username": username,
        "name": name,
        "lastname": lastname,
        "dni": dni,
        "phone": phone,
        "address": address
    }

    user = create_user(user_data)

    default_role = get_role_by_name("USER")
    if default_role:
        user.roles.append(default_role)
        db.session.commit()

    return user
