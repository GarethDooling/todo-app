from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    submit = SubmitField('Add Team')

class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    submit = SubmitField('Update')