from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class PitchForm(FlaskForm):
    pitch = TextAreaField('Enter your Pitch')
    name = StringField('Enter your name', validators=[DataRequired()])
    submit = SubmitField('Pitch', validators=[DataRequired()])