from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Required, Email


class ShowSignUp(Form):
    """Creates the signup form from WTF"""
    first_name = StringField('First name', [validators.Length(min=3, max=10)])
    last_name = StringField('Last name', [validators.Length(min=3, max=12)])
    username = StringField('Username')
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms & Conditions')
    submit = SubmitField('Sign Up')

'''Login Form '''


class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')