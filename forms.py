from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Searchfor(FlaskForm):
    search = StringField('SearchField', validators=[DataRequired()])
    submit = SubmitField('Cerca')

class CPUSelect(FlaskForm):
    tipo = SelectField('Marca', choices=['AMD','INTEL'])
    submit = SubmitField('Cerca')