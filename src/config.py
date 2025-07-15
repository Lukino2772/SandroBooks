from os import path

class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db' + path.join(BASE_DIRECTORY, 'database.db')