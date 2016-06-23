from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin  # LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


'''Flask Login Create Login Page Config'''
"""login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login' """

'''Creating my models: users, ideas ,
comments and an optional idea categories model later'''


class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.first_name = first_name
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.pwdhash, password)

    def __repr__(self):
        return ' < User %r >' % self.username


#@login_manager.user_loader
# def user_loader(user_id):
#    return User.query.get(int(user_id))


'''Creating the Ideas Model '''


class Idea(db.Model):
    __tablename__ = 'idea'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(
        'Category', backref=db.backref('ideas', lazy='dynamic'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('ideas', lazy='dynamic'))

    def __init__(self, title, body, category, user, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category
        self.user = user

    def __repr__(self):
        return '<Idea %r>' % self.title

'''Creating the Idea Category Section for our ideas'''


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('comments', lazy='dynamic'))

    idea_id = db.Column(db.Integer, db.ForeignKey('idea.id'))
    idea = db.relationship(
        'Idea', backref=db.backref('comments', lazy='dynamic'))


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)

    idea_id = db.Column(db.Integer, db.ForeignKey('idea.id'))
    idea = db.relationship('Idea', backref=db.backref('votes', lazy='dynamic'))


if __name__ == "__main__":
    manager.run()
