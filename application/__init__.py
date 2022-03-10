from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = getenv('secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@<ip address>:3306/flash_demo'

db = SQLAlchemy(app)

import application.routes