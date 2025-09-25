from flask import Flask
from src.admin_views.base import SecureModelView
from src.config import Config
from src.ext import db, migrate, admin, api
from src.commands import init_db, populate_db
from src.models.user import User
from src.models.book import Book

COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    return app

def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask_admin
    admin.init_app(app)
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Book, db.session))

    #Flask_RestX
    api.init_app(app)