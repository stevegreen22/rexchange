from flask import Flask, render_template

import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# method that will return a connection


def getConn():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'rexchange'
    }
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(buffered=True)
        return cursor
    except Error as e:
        print("Error while connecting to the database", e)
    finally:
        if (connection.isConnected()):
            connection.close()
            print("Closed database connection")

# not a huge fan of this but not wanting to mix responsibilities of the methods


def getWelcomeName():
    myConnection = getConn()
    sqlQuery = 'SELECT * FROM members'  # will only return the one value
    myConnection.execute(sqlQuery)
    records = myConnection.fetchall()
    return records


@app.route("/")
def home():
    name = getWelcomeName()
    return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.run()
