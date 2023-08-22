from flask import Blueprint, render_template
from flask_app.forms.register import RegisterForm

bp = Blueprint("main", __name__)


@bp.get("/")
def home():
    form = RegisterForm()
    return render_template("index.html", form=form)
