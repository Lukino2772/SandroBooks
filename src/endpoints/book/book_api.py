from flask_restx import Resource, fields, reqparse
from src.ext import api
from src.models.book import Book
from src.enums import CoverType, Booktype, Audience

book_model = api.model('Book', {"id": fields.Integer, "title": fields.String, "image": fields.String})

parser = reqparse.RequestParser()
parser.add_argument('cover_type', type=str, choices=[e.value for e in CoverType], required=False)
parser.add_argument("audience", type=str, choices=[e.value for e in Audience], required=False)
parser.add_argument("book_type", type=str, choices=[e.value for e in Booktype], required=False)
parser.add_argument("search", type=str, required=False)
parser.add_argument("sort", type=int, required=False)

@api.route("/books")
class Book(Resource):
    @api.expect(book_model, validate=True)
    @api.marshal_list_with(book_model)
    def get(self):
        args = parser.parse_args()
        query = Book.query

        if args["audience"]:
            query = query.filter(Book.audience == args["audience"])
        if args["book_type"]:
            query = query.filter(Book.book_type == args["book_type"])
        if args["cover_type"]:
            query = query.filter(Book.cover_type == args["cover_type"])
        if args["search"]:
            query = query.filter(Book.title.ilike(f"%{args['search']}%"))

        if args["sort"] == "free":
            query = query.filter(Book.price == 0)
        elif args["sort"] == "price_desc":
            query = query.filter(Book.price.desc())
        elif args["sort"] == "price_asc":
            query = query.filter(Book.price.asc())
        elif args["sort"] == "date_desc":
            query = query.filter(Book.date.desc())
        elif args["sort"] == "date_asc":
            query = query.filter(Book.date.asc())

        book = query.all()
        return [{"id" : b.id, "title" : b.title, "image" : b.image} for b in book]