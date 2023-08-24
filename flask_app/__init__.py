from os import environ
from flask import Flask
from flask_app.blueprints.main import bp as main
from flask_app.blueprints.auth import bp as auth
from dotenv import load_dotenv
from flask_app.extensions import db

load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    app.register_blueprint(main)
    app.register_blueprint(auth)

    db.init_app(app)

    with app.app_context():
        from flask_app.models.user import User

        db.create_all()

    return app
