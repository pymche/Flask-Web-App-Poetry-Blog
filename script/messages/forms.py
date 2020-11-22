from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

# Message Form
class MessageForm(FlaskForm): 
    name = StringField('Name', validators=[DataRequired()])
    letter = TextAreaField('Message', validators=[DataRequired()]) 
    submit = SubmitField('Submit')