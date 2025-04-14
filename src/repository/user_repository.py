from src.db import db
from src.models.user_model import User

class UserRepository:

    def add(self, data):
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get(self, user_id):
        return User.query.get(user_id)

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all(self):
        return User.query.all()

    def update(self, user, data):
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        db.session.commit()
        return user

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
