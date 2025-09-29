from flask import Blueprint, render_template, redirect, url_for, request, flash
from src.views.auth.forms import LoginForm
from src.models.user import User
from flask_login import login_user, logout_user

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
            return redirect(url_for("admin.index"))
        else:
            flash("Username or password is incorrect", "danger")
    return render_template("auth/login.html", form=form)

@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
