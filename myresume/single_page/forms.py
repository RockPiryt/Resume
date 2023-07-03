from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label=" ", validators=[DataRequired()])
    email= EmailField(label=" ", validators=[DataRequired()])
    subject = StringField(label=" ", validators=[DataRequired()])
    message = TextAreaField(label=" ", validators=[DataRequired()])
    submit = SubmitField(label="Submit")