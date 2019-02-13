from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# method that will return a connection


def getName():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'rexchange'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM members')
    results = cursor.fetchone()
    cursor.close()
    connection.close()

    return results[0]


@app.route('/')
def indexPage():
    name = getName()
    return f'Hello, {name}!'


@app.route('/template')
def templatePage():
    name = getName()
    return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
