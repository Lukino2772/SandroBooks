from src.ext import db

class BaseModel(db.Model):
    __abstract__ = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def create(self, commit=True):
        db.session.add(self)
        if commit:
            self.save()

    def save(self, commit=True):
        db.session.commit()

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            self.save()
