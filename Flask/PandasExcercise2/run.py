import os
from analyzer import create_app

env = os.environ.get('ANALYZER_CONFIG', 'development')
app = create_app('config.%sConfig' % env.capitalize())

if __name__ == '__main__':
    app.run()
