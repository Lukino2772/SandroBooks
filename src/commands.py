from flask.cli import with_appcontext
from src.models.book import Book
from src.ext import db
import click

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo('Initializing database...')

    db.drop_all()
    db.create_all()

    click.echo('Database initialized...')

@click.command("populate_db")
@with_appcontext
def populate_db():

    books = [
        {"id": 0, "title": "დიდი მოგზაურობა", "price": "32", "img": "book1.png"},
        {"id": 1, "title": "Amare La vita", "price": "31", "img": "book2.png"},
        {"id": 2, "title": "ქაოსიდან კოსმოსამდე", "price": "30", "img": "book3.png"},
        {"id": 3, "title": "იესეს ხის საკითხავები", "price": "29", "img": "book4.png"},
    ]

    for book in books:
        new_book = Book(
            title=book["title"],
            price=book["price"],
            image=book["img"],
            description="No description available",
            publication_year=None,
            page_count=None,
            format=None,
            ISBN=None,
            cover_type=None,
            online_link=None,
            audio_link=None,
            android_link=None,
            ios_link=None,
            about_series=None
        )
        db.session.add(new_book)
    db.session.commit()


