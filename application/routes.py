from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Correctword, User, Guess
from application.forms import AddProject, AddToDo
from datetime import date, timedelta