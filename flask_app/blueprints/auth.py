from flask import Blueprint, render_template, redirect
from flask_app.forms.register import RegisterForm

bp = Blueprint(
    "auth",
    __name__,
)


@bp.route("/auth/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return redirect("/auth/register")

    return render_template("/auth/register.html", form=form)


@bp.route("/auth/login", methods=["POST", "GET"])
def login():
    form = RegisterForm()

    if form.validate_on_submit():
        return redirect("/auth/login")

    return render_template("/auth/login.html", form=form)
