from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label=" ", validators=[DataRequired()])
    email= StringField(label=" ", validators=[DataRequired(), Email(message="Please enter valid email") ])
    subject = StringField(label=" ", validators=[DataRequired()])
    message = TextAreaField(label=" ", validators=[DataRequired()])
    submit = SubmitField(label="Submit")