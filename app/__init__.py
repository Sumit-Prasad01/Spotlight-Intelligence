from flask import Flask
from dotenv import load_dotenv
import os

from app.routes import main

def create_app():

    load_dotenv()
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))

    app = Flask(__name__, template_folder = template_path)

    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

    app.secret_key = os.getenv("SECRET_KEY", "default_secret")

    app.register_blueprint(main)

    return app