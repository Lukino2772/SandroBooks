from src.admin_views.book import BookView

def register_admin_views(admin, db):
    from src.models.book import Book
    admin.add_view(BookView(Book, db.session))