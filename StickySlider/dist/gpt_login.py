import mysql.connector
from mysql.connector import Error
from flask import Flask, request

app = Flask(__name__)

@app.route('/login.py', methods=['POST'])
def login():
    # Retrieve form data
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Connect to MySQL
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Insert user data into the database
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            values = (username, password, email)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return 'Login successful!'

    except Error as e:
        print("Error connecting to MySQL", e)

    return 'Login failed!'

if __name__ == '__main__':
    app.run()
