from os import path, environ

class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///books.db"
    SECRET_KEY = environ.get("SECRET_KEY")
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "assets")