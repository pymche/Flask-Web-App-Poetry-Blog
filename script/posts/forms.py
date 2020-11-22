from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# New Post Form
class NewPostForm(FlaskForm): 
    title = StringField('Title', validators=[DataRequired()])
    # date = DateField('Date', default='%d/%m/%Y')
    content = TextAreaField('Content', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

# Edit Post Form
class EditPostForm(FlaskForm): 
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()]) 
    submit = SubmitField('Make Changes')