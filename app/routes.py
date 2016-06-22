from flask import Flask, render_template
from forms import ShowSignUp

app = Flask(__name__)

@app.route('/')
def view_homepage():
    return render_template('index.html')


@app.route('/showSignUp', methods=['GET', 'POST'])
def register():
    form = ShowSignUp(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.first_name.data,form.last_name.data,form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thank You for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
	app.run(debug = True)