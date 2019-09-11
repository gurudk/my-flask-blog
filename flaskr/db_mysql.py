import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_pymysql import MySQL

mysqldb = MySQL()


def get_db():
    if 'db' not in g:
        g.db = mysqldb.connection

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema_mysql.sql') as f:
        db.cursor().execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    print('init-dbzzzzzzzzzzzzzzzzzzzzzz!')
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    mysqldb.init_app(app)
    print('init app kwargs:',app.config['pymysql_kwargs'])
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


