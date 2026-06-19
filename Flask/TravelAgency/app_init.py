import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base
import config

db = SQLAlchemy(model_class=Base)
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask("TravelAgency", template_folder="templates")

def create_app(views):
    app.secret_key = "GTYlv>K]0=otL=B`@z^s"
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
    app.register_blueprint(views.bp)
    with app.app_context():
        db.init_app(app)
    return app 

