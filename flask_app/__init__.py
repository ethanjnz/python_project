from os import environ
from flask import Flask
from flask_app.blueprints.main import bp as main
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")


def create_app():
    app = Flask(__name__)
    app.secret_key = "SECRET_KEY"

    app.register_blueprint(main)

    return app
