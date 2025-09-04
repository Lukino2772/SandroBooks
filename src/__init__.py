from flask import Flask
from src.ext import db, login_manager
from src.config import Config
from src.commands import init_db, populate_db

from src.blueprints.admin import admin_bp

COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "admin.login"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id: str):
        from src.models.user import User
        try:
            return User.query.get(int(user_id))
        except Exception:
            return None

def register_blueprints(app):
    app.register_blueprint(admin_bp)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
