from flask import Flask

"""Create and configure an instance of the analyzer application."""
app = Flask(__name__)

app.config.from_object(config)

app.add_url_rule("/", endpoint="hello")
