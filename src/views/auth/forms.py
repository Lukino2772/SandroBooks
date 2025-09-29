from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    login = SubmitField("Login")
