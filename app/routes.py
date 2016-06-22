from flask import Flask, render_template, url_for, request, flash, redirect
from models import db, User
from forms import ShowSignUp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

app.secret_key = "development-key"


@app.route('/')
def view_homepage():
    return render_template('index.html')


@app.route('/about')
def view_about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = ShowSignUp(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.first_name.data,
                    form.last_name.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        flash('Thanks for registering')
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
