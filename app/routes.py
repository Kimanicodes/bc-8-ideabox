from flask import Flask, render_template, url_for, request, flash, redirect, session, abort
from models import db, User, Idea
from forms import ShowSignUp, LoginForm, IdeaForm
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


@app.route('/show')
@login_required
def show():
    pass

@app.route('/about')
def view_about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_log = LoginForm()
    if form_log.validate_on_submit():

        user = User.query.filter_by(email=form_log.email.data).first()
        if user is not None and user.check_password_hash(form_log.password.data):
            login_user(user, form_log.remember_me.data)
            return redirect(request.args.get('next') or url_for('view_homepage'))

        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form_log)


@app.route('/feed')
@login_required
def get_feed():
    user_id = session.get('user_id')
    if not user_id:
        abort(403)
    user = User.query.filter_by(id=int(user_id)).first()
    ideas = user.ideas.all()
    return render_template('Feed.html', ideas=ideas)


@app.route('/new_idea', methods=['GET', 'POST'])
@login_required
def new_idea():
    form = IdeaForm()

    if request.method == 'POST' and form.validate_on_submit():
        user_id = session.get('user_id')
        if not user_id:
            abort(403)
        user = User.query.filter_by(id=int(user_id)).first()
        idea = Idea(title=form.title.data,
                    body=form.body.data,
                    user=user)
        db.session.add(idea)
        db.session.commit()
        return redirect(url_for('get_feed'))
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


@app.route('/home')
@login_required
def home():
    return render_template('home.html')



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


if __name__ == "__main__":
    app.run(debug=True)
