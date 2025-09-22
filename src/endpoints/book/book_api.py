from random import choices

from flask_restx import Resource, fields, reqparse
from src.ext import api, db
from src.models.book import Book
from src.enums import CoverType, Booktype, Audience

parser = reqparse.RequestParser()
parser.add_argument('cover_type', type=str, choices=[e.value for e in CoverType], required=False)
parser.add_argument("audience", type=str, choices=[e.value for e in Audience], required=False)
parser.add_argument("book_type", type=str, choices=[e.value for e in Booktype], required=False)
parser.add_argument("search", type=str, required=False)
parser.add_argument("sort", type=int, required=False)

@api.route("/books")
class Book(Resource):
    def get(self):
        book = Book.query.all()
        return book