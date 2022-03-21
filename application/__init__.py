from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.142.14.54:3306/wordle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import application.routes