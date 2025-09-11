from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileSize


class BookForm(FlaskForm):
    name = StringField("Enter Book Name")
    price = IntegerField("Enter Book Price")
    image = FileField("Upload Book Image", validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Add Book")