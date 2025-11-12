from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Logged in Successfully!", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password...", category="error")
        else:
            flash("Email does not exist. Please Sign Up!", category="error")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists. Please login!", category="error")
        elif not email or not first_name or not password1 or not password2:
            flash("All fields are compulsory to fill!", category="error")
        elif len(password1) < 6:
            flash("Password must be greater than 5 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = User(email=email, 
                            first_name=first_name, 
                            password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)