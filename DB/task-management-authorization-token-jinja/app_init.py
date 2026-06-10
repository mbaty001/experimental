from flask import Flask
import db
app = Flask("TaskManager", template_folder="templates")

def create_app(views, auth):
    app.register_blueprint(views.bp)
    app.register_blueprint(auth.bp)
    with app.app_context():
        db.init_app(app)
    app.secret_key = "GTYlv>K]0=otL=B`@z^s"
    return app
