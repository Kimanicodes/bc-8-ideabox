from flask import render_template
from manage import db
from forms import ShowSignUp

@ideabox_app.route('/')
def view_homepage():
    return render_template('index.html')


#@ideabox_app.route('/showSignUp', methods=['GET', 'POST'])
#def register():
#    form = ShowSignUp(request.form)
#    if request.method == 'POST' and form.validate():
#        user = User(form.username.data, form.first_name.data,form.last_name.data,form.email.data,
#                    form.password.data)
#        db_session.add(user)
#        flash('Thank You for registering!')
#        return redirect(url_for('login'))
#    return render_template('register.html', form=form)