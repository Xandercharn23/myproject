from flask import Flask

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

from flask_mysqldb import MySQL
mysql = MySQL(app)

from appfolder import routes