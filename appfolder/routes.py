from tkinter import _Cursor
import MySQLdb
from colorama import Cursor
from flask import app, render_template


@app.route('/')
def index():
        cursor = MySQLdb.connection.cursor(),
        products = _Cursor.fetchall()
        print(products)
        Cursor.close(),
        return render_template('index.html', products=products)