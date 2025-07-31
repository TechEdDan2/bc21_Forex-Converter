from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError

with open('static/codes.txt') as f:
    VALID_CURRENCY_CODES = set(code.strip().upper() for code in f.read().split(',') if code.strip())

def valid_currency_code(form, field):
    if field.data.upper() not in VALID_CURRENCY_CODES:
        raise ValidationError('Invalid currency code.')

class convertCurrency(FlaskForm):
    """ Convert one currency to another """
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)], places=2)
    from_currency = StringField('From Currency', validators=[DataRequired(), Length(min=3, max=3), valid_currency_code])
    to_currency = StringField('To Currency', validators=[DataRequired(), Length(min=3, max=3), valid_currency_code])   
   
