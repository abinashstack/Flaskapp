from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import forms
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY']='secret-key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db=SQLAlchemy(app)
from routes import *


if __name__ == "__main__":
    app.run(debug=True)