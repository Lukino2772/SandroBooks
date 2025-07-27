from flask import Flask
from src.ext import db
from src.config import Config
from src.commands import init_db

COMMANDS = [init_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)