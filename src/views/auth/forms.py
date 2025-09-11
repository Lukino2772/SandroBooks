from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField, RadioField, SelectField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    login = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired("მომხმარებლის სახელის ველის შევსება სავალდებულოა"), length(min=3, max=32)])
    password = PasswordField("Enter Password", validators=[DataRequired("პაროლის ველის შევსება სავალდებულოა"), length(min=8, max=32)])
    repeat_password = PasswordField("Confirm Password", validators=[DataRequired("განმეორებითი პაროლის ველის შევსება სავალდებულოა"), equal_to("password","პაროლები არ ემთხვევა ერთმანეთს")])

    birthday = DateField("Enter Birthday", validators=[DataRequired()])
    gender = RadioField("Enter Gender", choices=[(0, "Male"), (1, "Female")], validators=[DataRequired()])
    country = SelectField("Enter Country", choices=["Georgia", "Germany", "United States"], validators=[DataRequired()])


    submit = SubmitField("Register")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True
            if char in ascii_lowercase:
                contains_lowercase = True
            if char in digits:
                contains_digits = True
            if char in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
        if not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს რიცხვებს")
        if not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")