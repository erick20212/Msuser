from flask import Flask

from src.controller.permission_controller import permission_bp
from src.controller.role_controller import role_bp
from src.db import db
from src.config.config import Config
from src.controller.user_controller import user_bp
from src.controller.auth_controller import auth_bp
from flask_cors import CORS



import src.models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # 🛡️ Habilita CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("✅ Tablas creadas correctamente.")

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(role_bp, url_prefix='/roles')
    app.register_blueprint(permission_bp, url_prefix='/permissions')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
