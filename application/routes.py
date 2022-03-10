from collections import UserList, Counter
from contextvars import ContextVar
from distutils.log import Log
import re, time
from flask import redirect, render_template_string, url_for, render_template, request
from application import app, db
from application.models import Correctwords, User, Guess, Loggeduser
from application.forms import RegisterUser, Login, Addwordle, Deleteword, Update, Search
@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    message = None

    # time.sleep(1)
    # res = Loggeduser(log=3)
    # db.session.add(res)
    # db.session.commit()
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
            # newlog = Loggeduser.query.get(1)
            # Loggeduser.query.delete()
            f = Loggeduser.query.get(1)
            # f = f.join(str(k) for k in Loggeduser.query.all())
            # # return f'{f}'
            if f is not None:
                update = Loggeduser.query.get(1)
                update.log = user_list[0]
                # db.session.add(update)
                db.session.commit()
                log = Loggeduser.query.get(1)
                # return f'{f} + {log} + {user_list[0]}'
            else:
                newlog = Loggeduser(log=user_list[0])
            # newlog = user_list[0]
                db.session.add(newlog)
                db.session.commit()
            # return f'{log}'
            return render_template('index.html')
            # return redirect(url_for('home', list=log))
        else:
            return render_template('login.html', message = "Incorrect password", form = form)
    # passlog = User.query.filter_by(password=password_)
        #     if passlog.password == password:
        #             return redirect(url_for('home'))
        #     else: 
        #             return render_template('login.html', message = "Incorrect password", form = form)
        # else:
        #     return render_template('login.html', message = "Username not found", form = form)
    return render_template('login.html', message = "login to continue or " , form = form)

# @app.route('/test')
# def test():
#     x = ''
#     log = Loggeduser.query.all()
#     return f'{log}'
#     username_='spiffen'
#     # x = x.join(str(t) for t in User.query.filter_by(username=username_))
#     test = x.split(',')
#     # return test[1]
#     # return '<br>'.join(str(t) for t in User.query.all())
#     # return '<br>'.join(str(t) for t in Correctwords.query.all())
#     user3 = list(Guess.query.all())
#     return f'{user3[0]}'
#     return '<br>'.join(str(t) for t in User.query.filter_by(username='test'))

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

@app.route('/wordlestats', methods=['GET','POST'])
def wordlestats():
    form = Search()
    test = []
    list = ''
    g = 0
    log = str(Loggeduser.query.get(1))
    test = db.session.query(Guess, Correctwords).join(Correctwords).filter_by(userid_fk=log).all()
    # test = Guess.query.all()
    # return f'{test[1][0]}'
    g = len(test[0]) - 1
    # return f'{g}'
    while g >= 0:
        g = g - 1
        list += (str(test[g][0])) + ','
    list2 = list.split(',')
    count = Counter(list2)
    count = str(count)
    count = count.replace('Counter({', '')
    count = count.replace('})','')
    count = count.replace("'", "")
    countList = count.split(',')
    # return f'{countList[5]}'
    common = countList[0].split(':')
    # return f'{count}'
    message = "Your most used word is " + common[0] + " using it " + common[1] + " times"
    if request.method == 'POST':
        serch = form.search.data
        for i in countList:
            b = i.split(':')
            b[0] = b[0].replace(' ', '')
            print(b)
            # return f'{b[0]}'
            if serch == b[0]:
                message = "You have used the word '" + serch + "' " + b[1] + " times"
                return render_template('stats.html',message = message, form=form)
        return render_template('stats.html', message ='word not found', form=form)
    return render_template('stats.html', message = message, form=form)



    # g = test[1][0]
    # g = str(g)
    # list = g.split(',')
    # count = count + Counter(list)

    # return f'{countList[0]}'
    # return f'<br>'.join(str(t) for t in test[1])

    # return f'<br>'.join(str(t) for t in Guess.query.all())

@app.route('/deleteword', methods=['GET','POST'])
def deleteword():
    form = Deleteword()
    wordlist = Correctwords.query.all()
    form.word_.choices.extend([(words.correct_id, str(words.correctword)) for words in wordlist])
    if form.delete.data == True:
        deletew = form.word_.data
        delwords = Guess.query.get(deletew)
        # return f'{delwords}'
        db.session.delete(delwords)
        db.session.commit()
        return render_template('deleteword.html', form=form, message= 'words deleted')
    elif request.method == 'POST':
        deletew = form.word_.data
        delwords = Guess.query.get(deletew)
        return render_template('deleteword.html', form=form, message=delwords)
    return render_template('deleteword.html', form=form)
    # return f'{list}'

@app.route('/updatewords', methods=['GET','POST'])
def updatewords():
    form = Update()
    wordlist = Correctwords.query.all()
    wordup = Guess.query.get(1)
    message = "Click submit to see what guesses to update"
    form.word_.choices.extend([(words.correct_id, str(words.correctword)) for words in wordlist])
    if request.method == 'POST':
        updateid = form.word_.data
        wordup = Guess.query.get(updateid)
        message = wordup
        if form.update_.data == True:
            wordup.guess1 = form.guess1.data
            wordup.guess2 = form.guess2.data
            wordup.guess3 = form.guess3.data
            wordup.guess4 = form.guess4.data
            wordup.guess5 = form.guess5.data
            wordup.guess6 = form.guess6.data
            db.session.commit()
            return render_template('update.html', form=form, message="words updated")
        return render_template('update.html', form=form, message=message)
    return render_template('update.html', form=form, message=message)

    

@app.route('/addwordle', methods=['GET','POST'])
def addwordle():
    x = ''
    form = Addwordle()
    if request.method == 'POST':
        log = str(Loggeduser.query.get(1))
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