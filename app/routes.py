from flask import Flask, render_template, url_for, request, flash, redirect, session
from models import db, User
from forms import ShowSignUp, LoginForm, Idea
from flask_login import login_user, LoginManager, login_required, UserMixin, current_user, logout_user
# from . import flask_login  LoginManager


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

'''
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
'''

app.secret_key = "development-key"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def view_homepage():
    return render_template('index.html')


@app.route('/feed')
@login_required
def feed():
    #flash('Please Login to continue!')
    # return redirect(url_for('login'))
    return render_template('Feed.html')


@app.route('/about')
def view_about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_log = LoginForm()
    if form_log.validate_on_submit():

        user = User.query.filter_by(email=form_log.email.data).first()
        #import pdb; pdb.set_trace()
        if user is not None and user.check_password_hash(form_log.password.data):
            login_user(user, form_log.remember_me.data)
            return redirect(request.args.get('next') or url_for('view_about'))

        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form_log)


@app.route('/new_idea', methods=['GET', 'POST'])
@login_required
def new_idea():
    form = Idea()
    if form.validate_on_submit():
        idea = Idea(title=form.title.data,
                    category=form.category.data,
                    body=form.body.data)
        db.session.add(idea)
        db.session.commit()
    return render_template('new_idea.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('view_homepage'))


@app.route('/views')
@login_required
def secret():
    return redirect(url_for('view_about'))

#@app.route('/secret')
#@login_required
# def secret():
#    return 'Only authenticated users are allowed!'


@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = ShowSignUp(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        session['email'] = user.email
        flash('Thanks for registering. Please Login to continue!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

    #form = ShowSignUp(request.form)
    # if request.method == 'POST' and form.validate():
    #    user = User(form.username.data, form.first_name.data,form.last_name.data,form.email.data,
    #                form.password.data)
    #    db_session.add(user)
    #    flash('Thank You for registering!')
    #    return redirect(url_for('login'))
    # return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
