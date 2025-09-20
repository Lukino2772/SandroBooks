from flask import Blueprint, render_template, url_for, redirect
from uuid import uuid4
from os import path
from src.views.book.forms import BookForm
from src.models.book import Book
from src.config import Config
from src.utils import admin_required


book_blueprint = Blueprint("users", __name__)

@book_blueprint.route("/add_book", methods=["GET", "POST"])
@admin_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        file = form.image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))
        new_book = Book(title=form.title.data, price=form.price.data, image=filename)

        new_book.create()

        return redirect(url_for("main.index"))
    return render_template("book/add_book.html", form=form)

@book_blueprint.route("/edit_book/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_book(id):
    book = Book.query.get(id)

    form = BookForm(title=book.title, price=book.price)
    if form.validate_on_submit():

        book.title = form.title.data
        book.price = form.price.data
        book.save()

        if form.image.data:
            file = form.image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(Config.UPLOAD_PATH, filename))

            book.image = filename

        return redirect(url_for("main.index"))

    return render_template("book/add_book.html", form=form)

@book_blueprint.route("/delete_book/<int:id>")
@admin_required
def delete_book(id):

    book = Book.query.get(id)
    book.delete()

    return redirect(url_for("main.index"))

@book_blueprint.route("/view/<int:book_id>")
def view_book(book_id):
    chosen_book = Book.query.get(book_id)
    return render_template("book/view_book.html", book=chosen_book)