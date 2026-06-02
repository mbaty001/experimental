import views
import auth
from app import app

if __name__ == "__main__":
    app.secret_key = "^%&HGJTYTjhjkgh455646-0-7&*^%$#@!~"
    app.register_blueprint(views.bp)
    app.register_blueprint(auth.bp)
    app.run(debug=True)