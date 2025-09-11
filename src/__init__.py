from flask import Flask
from src.config import Config
from src.ext import db, migrate, login_manager
from src.views import main_blueprint, auth_blueprint, book_blueprint
from src.commands import init_db, populate_db
from src.models.user import User

BLUEPRINTS = [main_blueprint, auth_blueprint, book_blueprint]
COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    #Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)