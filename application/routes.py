from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Correctwords, User, Guess
from application.forms import RegisterUser, Login

@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    message = None
    if request.method == 'POST':
        username_ = form.username.data
        password_ = form.passw.data 
        # return username_
        x = ''
        x = x.join(str(t) for t in User.query.filter_by(username=username_))
        # return x
        user_list = x.split(',')
        # return f'{user_list[1]} + {user_list[0]} + {username_} + {password_}'
        if user_list[1] == password_:
            return redirect(url_for('home'))
        # else:
            return render_template('login.html', message = "Incorrect password", form = form)
    # passlog = User.query.filter_by(password=password_)
        #     if passlog.password == password:
        #             return redirect(url_for('home'))
        #     else: 
        #             return render_template('login.html', message = "Incorrect password", form = form)
        # else:
        #     return render_template('login.html', message = "Username not found", form = form)
    return render_template('login.html', message = "login to continue or " , form = form )

@app.route('/test')
def test():
    x = ''
    username_='spiffen'
    x = x.join(str(t) for t in User.query.filter_by(username=username_))
    test = x.split(',')
    return test[1]
    # return '<br>'.join(str(t) for t in User.query.all())
    # return '<br>'.join(str(t) for t in User.query.filter_by(username='test'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser()
    if request.method == 'POST':
        user = form.user.data
        password_ = form.password.data
        new_user = User(username = user, password = password_)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


@app.route('/home')
def home():
    return render_template('index.html')