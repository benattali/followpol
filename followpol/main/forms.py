from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TwitterHandleForm(FlaskForm):
    handle = StringField('Handle', validators=[DataRequired()])
    submit = SubmitField('Search')