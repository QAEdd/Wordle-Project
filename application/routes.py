from collections import UserList, Counter
import re
from flask import redirect, render_template_string, url_for, render_template, request
from application import app, db
from application.models import Correctwords, User, Guess
from application.forms import RegisterUser, Login, Addwordle
log = 0
@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    global log
    message = None
    if request.method == 'POST':
        username_ = form.username.data
        password_ = form.passw.data 
        # return username_
        x = ''
        x = x.join(str(t) for t in User.query.filter_by(username=username_))
        # return x
        user_list = x.split(',')
        # user_list[1] = user_list[1].replace(" ", "")
        # return f'{user_list[1]} {user_list[2]} {username_} {password_}'
        if user_list[2] == password_:
            log = user_list[0]
            
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message = "Incorrect password", form = form)
    # passlog = User.query.filter_by(password=password_)
        #     if passlog.password == password:
        #             return redirect(url_for('home'))
        #     else: 
        #             return render_template('login.html', message = "Incorrect password", form = form)
        # else:
        #     return render_template('login.html', message = "Username not found", form = form)
    return render_template('login.html', message = "login to continue or " , form = form, log=log )

@app.route('/test')
def test():
    x = ''
    username_='spiffen'
    # x = x.join(str(t) for t in User.query.filter_by(username=username_))
    test = x.split(',')
    # return test[1]
    # return '<br>'.join(str(t) for t in User.query.all())
    # return '<br>'.join(str(t) for t in Correctwords.query.all())
    user3 = list(Guess.query.all())
    return f'{user3[0]}'
    return '<br>'.join(str(t) for t in User.query.filter_by(username='test'))

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

@app.route('/wordlestats')
def wordlestats():
    test = []
    list = ''
    g = 0
    test = db.session.query(Guess, Correctwords).join(Correctwords).filter_by(userid_fk=log)
    g = len(test[1])
    while g >= 0:
        list += (str(test[g][0])) + ','
        g = g - 1
    list2 = list.split(',')
    count = Counter(list2)
        
    # g = test[1][0]
    # g = str(g)
    # list = g.split(',')
    # count = count + Counter(list)

    return f'{count}'
    # return f'<br>'.join(str(t) for t in test[1])

    return f'<br>'.join(str(t) for t in Guess.query.all())

@app.route('/deleteword')
def deleteword():
    x = Correctwords.query.order_by(Correctwords.correctword).all()
    c = []
    list = []
    for i in x:
        b = str(i)
        c = b.split(',')
        list.append(c[2])
    
    return f'{list}'

@app.route('/addwordle', methods=['GET','POST'])
def addwordle():
    x = ''
    form = Addwordle()
    if request.method == 'POST':
        correctword_ = form.correctword.data
        add_correct = Correctwords(userid_fk=log,correctword = correctword_)
        db.session.add(add_correct)
        db.session.commit()
        x = x.join(str(t) for t in Correctwords.query.filter_by(correctword=correctword_))
        y = x.split(',')
        Cword = y[0]
        gues1 = form.guess1.data
        gues2 = form.guess2.data
        gues3 = form.guess3.data
        gues4 = form.guess4.data
        gues5 = form.guess5.data
        gues6 = form.guess6.data
        add_word = Guess(guess1 = gues1, guess2 = gues2, guess3 = gues3, guess4 = gues4, guess5 = gues5, guess6=gues6,correctword_fk=Cword) 
        db.session.add(add_word)
        db.session.commit()
        return redirect(url_for('home'))   
    return render_template('addwordle.html', form = form)


@app.route('/home')
def home():
    return render_template('index.html')