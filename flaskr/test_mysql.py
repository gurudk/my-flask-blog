from flask import Flask
from flask_pymysql import MySQL

app = Flask(__name__)

pymysql_connect_kwargs = {'user': 'beconlab',
                          'password': 'beconlab',
                          'host': '127.0.0.1',
                          'database': 'beconlab',
                          'cursorclass': 'DictCursor'}

app.config['pymysql_kwargs'] = pymysql_connect_kwargs

db = MySQL(app)


@app.route('/')
def users():
    cur = db.connection.cursor()
    cur.execute(
        "select * from user"
    )

    rv = cur.fetchone()
    print(rv)
    return str(rv)


if __name__ == '__main__':
    app.run(debug=True)

