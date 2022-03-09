from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    correct_back = db.relationship('Correctwords', backref='User')
    def __str__(self):
        return f"{self.user_id},{self.username},{self.password}"

class Correctwords(db.Model):
    correct_id = db.Column(db.Integer, primary_key = True)
    userid_fk = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    correctword = db.Column(db.String(5))
    guesses = db.relationship('Guess', backref='Correctwords')
    def __str__(self):
        return f"{self.correct_id},{self.userid_fk},{self.correctword}"

class Guess(db.Model):
    guess_id = db.Column(db.Integer, primary_key = True)
    correctword_fk = db.Column(db.Integer, db.ForeignKey('correctwords.correct_id'))
    guess1 = db.Column(db.String(5))
    guess2 = db.Column(db.String(5))
    guess3 = db.Column(db.String(5))
    guess4 = db.Column(db.String(5))
    guess5 = db.Column(db.String(5))
    guess6 = db.Column(db.String(5))
    def __str__(self):
        return f"{self.guess1},{self.guess2},{self.guess3},{self.guess4},{self.guess5},{self.guess6}"

class Loggeduser(db.Model):
    log_id = db.Column(db.Integer, primary_key = True)
    log = db.Column(db.Integer)
    def __str__(self):
        return f'{self.log}'

