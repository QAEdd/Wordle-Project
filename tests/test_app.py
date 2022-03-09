from urllib import response
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import User, Correctwords, Guess, Loggeduser
from application.routes import wordlestats

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "test secret key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        sample_User = User(username="SampleUser",password="SamplePass")
        sample_Correct = Correctwords(userid_fk = 1, correctword="plant")
        sample_Guess  = Guess(correctword_fk = 1, guess1="print",guess2="gleam",guess3="joint",guess4="jokes",guess5="gnome",guess6="plant", )
        sample_log = Loggeduser(log=1)

        db.session.add(sample_User)
        db.session.add(sample_log)
        db.session.add(sample_Correct)
        db.session.add(sample_Guess)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestLogin(TestBase):
    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assert200(response)

    def test_login_post(self):
        response = self.client.post(
            url_for('login'),
            data = dict(username="SampleUser", password="SamplePass"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'1',response.data)

    def test_login_fail(self):
        response = self.client.get(url_for('login'),
        data = dict(username="SampleUser",password="nothtere"))
        self.assert200(response)

    
class TestRegister(TestBase):
    def test_register_get(self):
        response = self.client.get(url_for('register'))
        self.assert200(response)

    def test_register_post(self):
        response = self.client.post(
            url_for('register'),
            data = dict(user="sampleu",password="samplep", confirmpass="samplep"),
            follow_redirects = True
        )
        self.assert200(response)

class TestAddWordle(TestBase):
    def test_addwordle_get(self):
        response = self.client.get(url_for('addwordle'))
        self.assert200(response)

    def test_addwordle_post(self):
        response = self.client.post(
            url_for('addwordle'),
            data = dict(correctword="tests", guess1="words",guess2="pains", guess3="plank", guess4="women",guess5="spiny",guess6="shiny"),
            follow_redirects = True
        )
        self.assert200(response)

class TestUpdateWordle(TestBase):
    def test_updatewordle_get(self):
        response = self.client.get(url_for('updatewords'))
        self.assert200(response)

    def test_updatewordle_post(self):
        response = self.client.post(url_for('updatewords'),
        data = dict(word_="plant", guess1="words",guess2="pains", guess3="plank", guess4="women",guess5="spiny",guess6="shiny")
        )
        self.assert200(response)

class TestDeleteWordle(TestBase):
    def test_deletewordle_get(self):
        response = self.client.get(url_for('deleteword'))
        self.assert200(response)

    def test_deleteworlde_post(self):
        response = self.client.post(url_for('deleteword'),
        data = dict(word_='plant'))
        self.assert200(response)
    
    def test_deleteworlde_post(self):
        response = self.client.post(url_for('deleteword'),
        data = dict(deletew_='plant', delete=True))
        self.assert200(response)
        self.assertNotIn(b'print', response.data)


class TestSearchWordle(TestBase):
    def test_searchwordle_get(self):
        response = self.client.get(url_for('wordlestats'))
        self.assert200(response)

    def test_searchwordle_post(self):
        response = self.client.post(url_for('wordlestats'),
        data = dict(search='print'))
        self.assert200(response)

    def test_searchwordlefail_post(self):
        response = self.client.post(url_for('wordlestats'),
        data = dict(search='yes'))
        self.assert200(response)

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)