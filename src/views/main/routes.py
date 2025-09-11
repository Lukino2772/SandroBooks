from flask import Blueprint, render_template
from src.models.book import Book

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def index():
    books = Book.query.all()

    return render_template("main/index.html", books=books)
@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")