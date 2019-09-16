from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password',
							 validators=[DataRequired(), Length(min=6)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log  In')