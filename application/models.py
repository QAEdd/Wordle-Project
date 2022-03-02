from application import db

class Correctwords(db.Model):
    correct_id = db.Column(db.Integer, primary_key = True)
    guessid_fk = db.Column(db.Integer, db.ForeignKey('guess_id'))
    userid_fk = db.Column(db.Integer, db.ForeignKey('user_id'))
    correctword = db.Column(db.String(5))

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Guess(db.Model):
    guess_id = db.Column(db.Integer, primary_key = True)
    correctword_fk = db.Column(db.Integer, db.ForeignKey('correct_id'))
    guess1 = db.Column(db.String(5))
    guess2 = db.Column(db.String(5))
    guess3 = db.Column(db.String(5))
    guess4 = db.Column(db.String(5))
    guess5 = db.Column(db.String(5))
    guess6 = db.Column(db.String(5))
