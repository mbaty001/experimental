import os
from flask import Flask

app = Flask(__name__)

config_env = os.environ.get('CONFIG', 'development')
app.config.from_object(f'config.{config_env.capitalize()}Config')

from views import *

app.add_url_rule("/hello", endpoint="hello")

if __name__ == '__main__':
    app.run()
