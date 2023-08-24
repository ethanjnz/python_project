from flask import Blueprint, render_template, redirect
from flask_app.forms.register import RegisterForm

bp = Blueprint("main", __name__)


@bp.get("/")
def ret_redirect():
    return redirect("/welcome")


@bp.get("/welcome")
def home():
    return render_template("welcome.html")
