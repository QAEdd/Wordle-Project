from click import pass_context
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from datetime import date
from application.models import Correctwords, User, Guess

class RegisterUser(FlaskForm):
    user = StringField("Username: ")
    password = StringField("Password: ")
    confirmpass = StringField("Confirm Password: ")
    submit = SubmitField("Submit")


class Login(FlaskForm):
    username = StringField("Username: ")
    passw = StringField("Password: ")
    submit = SubmitField("Submit")