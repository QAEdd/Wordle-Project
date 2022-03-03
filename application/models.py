from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    correct_back = db.relationship('Correctwords', backref='User')

class Correctwords(db.Model):
    correct_id = db.Column(db.Integer, primary_key = True)
    userid_fk = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    correctword = db.Column(db.String(5))
    guesses = db.relationship('Guess', backref='Correctwords')

class Guess(db.Model):
    guess_id = db.Column(db.Integer, primary_key = True)
    correctword_fk = db.Column(db.Integer, db.ForeignKey('correctwords.correct_id'))
    guess1 = db.Column(db.String(5))
    guess2 = db.Column(db.String(5))
    guess3 = db.Column(db.String(5))
    guess4 = db.Column(db.String(5))
    guess5 = db.Column(db.String(5))
    guess6 = db.Column(db.String(5))

