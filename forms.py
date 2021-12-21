from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, BooleanField
from wtforms.validators import DataRequired, NumberRange

class Searchfor(FlaskForm):
    search = StringField('SearchField', validators=[DataRequired()])
    submit = SubmitField('Cerca')

class CPUSelect(FlaskForm):
    #marche:
    AMD = BooleanField('AMD')
    INTEL = BooleanField('Intel')
   #socket types:
    AM4 = BooleanField('AM4')
    lga =  BooleanField('LGA 1151')
   #wattaggi:
    sixfive = BooleanField('65 W')
    onehunfive = BooleanField('105 W')
   #max e min
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')

class CaseSelect(FlaskForm):
    Col = BooleanField('Cooler Master')
