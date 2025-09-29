from app import app
from src.ext import db
from src.models.user import User

with app.app_context():
    admin = User(username="admin", role="Admin")
    admin.password = "yourpassword"
    db.session.add(admin)
    db.session.commit()
    print("Admin user created!")
