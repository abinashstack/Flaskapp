from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    submit=SubmitField("Submit")
