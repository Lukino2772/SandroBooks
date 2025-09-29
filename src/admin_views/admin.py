from src.models.book import Book
from src import db, admin
from src.admin_views.book import BookView


admin.add_view(BookView(Book, db.session))