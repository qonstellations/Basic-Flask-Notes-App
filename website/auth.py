from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout page</p>"

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not email or not first_name or not password1 or not password2:
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
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")