from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from src.models.user import User

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("წარმატებით შეხვედი სისტემაში.", "success")
            next_url = request.args.get("next")
            return redirect(next_url or url_for("admin.dashboard"))
        flash("არასწორი მონაცემებია.", "danger")

    return render_template("admin/login.html")

@admin_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("გამოხვედი სისტემიდან.", "info")
    return redirect(url_for("admin.login"))

@admin_bp.route("/")
@login_required
def dashboard():
    return render_template("admin/dashboard.html")
