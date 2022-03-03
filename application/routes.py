from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Correctwords, User, Guess
from application.forms import RegisterUser, Login

@app.route('/', methods=['GET', 'POST'])
def login():
    
    form = Login()
    message = None
    if request.method == 'POST':
        username = form.username.data
        password = form.passw.data
        for i in User.query.filter_by(username):
            if username == i:
                passlog = User.query.filter_by(username)
                if passlog.password == password:
                    return redirect(url_for('home'))
                else: 
                    return render_template('login.html', message = "Incorrect password", form = form)
            else:
                return render_template('login.html', message = "Username not found", form = form)
    return render_template('login.html', message = "Enter a username and password to continue or ", form = form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser()
    if request.method == 'POST':
        user = form.user.data
        password = form.password.data
        new_user = User(username = user, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


@app.route('/home')
def home():
    return render_template('index.html')