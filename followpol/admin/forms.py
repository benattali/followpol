from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password',
							 validators=[DataRequired(), Length(min=6)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log  In')

class UploadCSV(FlaskForm):
    csv = FileField('Upload CSV', validators=[FileAllowed(['csv'])])
    submit = SubmitField('Upload')