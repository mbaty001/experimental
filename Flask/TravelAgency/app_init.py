import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config
from models import Base

db = SQLAlchemy(model_class=Base)
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask("TravelAgency", template_folder="templates")


def create_app(views):
    app.secret_key = "GTYlv>K]0=otL=B`@z^s"
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
    app.register_blueprint(views.bp_clients)
    app.register_blueprint(views.bp_itineraries)
    with app.app_context():
        db.init_app(app)
    return app
