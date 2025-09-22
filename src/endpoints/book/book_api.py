from flask_restx import Resource
from src.ext import api
from src.models.book import Book

@api.route("/books")
class Book(Resource):
    def get(self):
        book = Book.query.all()
        return book