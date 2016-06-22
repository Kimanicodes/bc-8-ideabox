from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email


class ShowSignUp(Form):
    """Creates the signup form from WTF"""
    first_name = StringField('First name', [validators.Length(min=8, max=25)])
    last_name = StringField('Last name', [validators.Length(min=8, max=35)])
    username = StringField('Username', )
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms & Conditions')
    submit = SubmitField('Sign Up')
