from flask import Blueprint, render_template, redirect, url_for, request, flash
from src.views.auth.forms import RegisterForm, LoginForm
from src.models.user import User
from flask_login import login_user, logout_user, current_user, login_required

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            next = request.args.get("next")
            login_user(user)
            if next:
                return redirect(next)
            flash("Logged in!", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Username or password is incorrect", "danger")
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

@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth_blueprint.route("/profile")
@login_required
def view_profile():
    return render_template("auth/profile.html")