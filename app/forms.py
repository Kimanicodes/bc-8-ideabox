from wtforms import Form, BooleanField, StringField, PasswordField, validators


class ShowSignUp(Form):
    """Creates the signup form from WTF"""
    first_name = StringField('first_name', [validators.Length(min=6, max=20)])
    last_name = StringField('last_name', [validators.Length(min=6, max=20)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
		validators.DataRequired(),
    	validators.EqualTo('confirm', message='Passwords must match')
    	])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms & Conditions', [validators.DataRequired()])
    




