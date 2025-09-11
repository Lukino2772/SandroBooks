# from src.ext import db
# from src.models.base_model import BaseModel
#
# class Book(BaseModel):
#     __tablename__ = 'books'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     description = db.Column(db.String, nullable=False)
#     price = db.Column(db.Float)
#     publication_year = db.Column(db.Integer)
#     page_count = db.Column(db.Integer)
#     format = db.Column(db.String)
#     ISBN = db.Column(db.Integer)
#     cover_type = db.Column(db.String)
#     online_link = db.Column(db.String)
#     audio_link = db.Column(db.String)
#     android_link = db.Column(db.String)
#     ios_link = db.Column(db.String)
#     about_series = db.Column(db.String)

from src.models.base import BaseModel
from src.ext import db

class Book(BaseModel):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)

