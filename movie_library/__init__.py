import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database

from werkzeug.datastructures import MultiDict

from movie_library.routes import pages

load_dotenv()

class CustomFlask(Flask):
    db: Database

def create_app():
    app = CustomFlask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )
    app.config["parameter_storage_class"] = MultiDict

    client = MongoClient(app.config["MONGODB_URI"])

    # Selecionando o banco de dados 'Movie_Watchlist'
    app.db = client["Movie_Watchlist"]

    # Registrando o blueprint 'pages'
    app.register_blueprint(pages)

    return app
