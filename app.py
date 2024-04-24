from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'mysql-container'  # Name of the MySQL container
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM mytable")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO mytable (name) VALUES (%s)", (name,))
    mysql.connection.commit()
    cursor.close()
    return 'Data inserted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)