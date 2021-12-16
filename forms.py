from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class Searchfor(FlaskForm):
    search = StringField('SearchField', validators=[DataRequired()])
    submit = SubmitField('Cerca')

class CPUSelect(FlaskForm):
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submit = SubmitField('Cerca')
