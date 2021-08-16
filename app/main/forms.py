from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.simple import TextAreaField



class PitchForm(FlaskForm):
    pitch = TextAreaField('Enter your Pitch')
    name = StringField('enter your name')
    submit = SubmitField('Pitch')