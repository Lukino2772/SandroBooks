from flask import Blueprint, render_template, redirect, url_for
from src.views.auth.forms import RegisterForm, LoginForm
from src.models.user import User
from flask_login import login_user

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("main.index"))
    return render_template("auth/login.html", form=form)

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()

    else:
        print(form.errors)
    return render_template("auth/register.html", form=form)