from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


'''Creating an instance of the flask class'''
ideabox_app = Flask(__name__)
'''This app uses sqllite'''
ideabox_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideabox.db'
ideabox_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(ideabox_app)
migrate = Migrate(ideabox_app, db)
manager = Manager(ideabox_app)
manager.add_command('db', MigrateCommand)


@ideabox_app.route('/')
def view_homepage():
    return render_template('index.html')

@ideabox_app.route('/showsignup')
def show_info():
	return render_template('showsignup.html')


if __name__ == "__main__":
    manager.run()
