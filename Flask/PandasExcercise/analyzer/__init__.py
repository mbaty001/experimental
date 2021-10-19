from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the analyzer application."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    from analyzer.views import hello

    app.add_url_rule("/", endpoint="hello")
    return app

