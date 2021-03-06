from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, BooleanField
from wtforms.validators import DataRequired, NumberRange


class Searchfor(FlaskForm):
    search = StringField('SearchField', validators=[DataRequired()])
    submit = SubmitField('Cerca')


class CPUSelect(FlaskForm):
    # marche:
    AMD = BooleanField('AMD')
    INTEL = BooleanField('Intel')
    # socket types:
    AM4 = BooleanField('AM4')
    lga = BooleanField('LGA 1151')
    # wattaggi:
    sixfive = BooleanField('65 W')
    onehunfive = BooleanField('105 W')
    onetwofive = BooleanField('125 W')
    # max e min
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class CaseSelect(FlaskForm):
    # marche:
    Col = BooleanField('Cooler Master')
    Shark = BooleanField('Sharkoon')
    Therm = BooleanField('Thermaltake')
    # model:
    ATX = BooleanField('ATX')
    mATX = BooleanField('mATX')
    # max e min
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class MoboSelect(FlaskForm):
    # marche:
    Asus = BooleanField("Asus")
    MSI = BooleanField("MSI")
    Giga = BooleanField("Gigabyte")
    # socket types:
    AM4 = BooleanField('AM4')
    lga = BooleanField('LGA 1151')
    # model:
    ATX = BooleanField('ATX')
    mATX = BooleanField('mATX')
    # clock ram:
    twofive = BooleanField("2500 Hz")
    fourfive = BooleanField("4500 Hz")
    fivetre = BooleanField("5300 Hz")
    # wattaggi:
    seventy = BooleanField('70 W')
    fifty = BooleanField('50 W')
    # max e min
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class PSUSelect(FlaskForm):
    Col = BooleanField('Cooler Master')
    Shark = BooleanField('Sharkoon')
    Cors = BooleanField('Corsair')

    sixfive = BooleanField('650 W')
    sevenfive = BooleanField('750 W')
    eightfive = BooleanField('850 W')

    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class CoolSelect(FlaskForm):
    # marche:
    Deep = BooleanField('DEEP COOL')
    Col = BooleanField('Cooler Maste')
    Cors = BooleanField('Corsair')

    AM4 = BooleanField('AM4')
    lga = BooleanField('LGA 1151')

    air = BooleanField("Aria")
    liq = BooleanField("Liquido")

    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class RAMSelect(FlaskForm):
    Col = BooleanField('Cooler Master')
    Cruc = BooleanField('Crucial')

    # clock ram:
    treetwo = BooleanField("3200 Hz")
    treesix = BooleanField("3600 Hz")

    # qt ram:
    six = BooleanField("16 Gb")
    tree = BooleanField("32 GB")

    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')


class MEMOSelect(FlaskForm):
    Cruc = BooleanField('Crucial')
    Sam = BooleanField('Samsung')
    Sea = BooleanField('Seagate')
    WD = BooleanField('WD')

    SSD = BooleanField('SSD')
    HD = BooleanField('Hard-Disk')

    quattro = BooleanField('480 GB')
    cinque = BooleanField('500 GB')
    mille = BooleanField('1 TB')

    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')

class GPUSelect(FlaskForm):

    # marche:
    Asus = BooleanField("Asus")
    xfx = BooleanField("XFX")
    Giga = BooleanField("Gigabyte")
    # prod:
    AMD = BooleanField('AMD')
    Nvidia = BooleanField('Nvdia')
    #Tipo:
    RX = BooleanField('RX')
    RTX = BooleanField('RTX')
    #costo :
    minmonet = DecimalField('MinField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    maxmonet = DecimalField('MaxField', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    submitf = SubmitField('Cerca')