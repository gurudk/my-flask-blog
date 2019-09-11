import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = b'_8#y1L"F4Q8z\n\xec]/'

    pymysql_connect_kwargs = {'user': 'beconlab',
                              'password': 'beconlab',
                              'host': '127.0.0.1',
                              'database': 'beconlab',
                              'cursorclass': 'DictCursor'}

    app.config['pymysql_kwargs'] = pymysql_connect_kwargs
    print('create app kwargs:', app.config['pymysql_kwargs'])

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # endure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db_mysql
    db_mysql.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

