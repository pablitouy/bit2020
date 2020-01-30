from flask import Flask, json , jsonify, render_template, request, redirect, url_for, flash
import pymysql
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

# initializations
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:37124796@localhost:3306/probit'

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '37124796'
app.config['MYSQL_DATABASE_DB'] = 'probit'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# settings
app.secret_key = "mysecretkey"
db = SQLAlchemy(app)

class Empresas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    direccion = db.Column(db.String(200))


# routes

@app.route('/empresas')
def Index():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM empresas")
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp

@app.route('/')
def home():
    return "pagina de inicio"




# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
