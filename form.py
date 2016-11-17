from flask_wtf import Form  
from wtforms import StringField, BooleanField, TextAreaField, validators,IntegerField
from wtforms.validators import InputRequired, Length

class SwapForm(Form):
    FromDay = StringField(u'From Day:', validators=[InputRequired(), Length(max=10)])
    ToDay = StringField(u'To Day:', validators=[InputRequired(), Length(max=10)])
    FromPeriod = IntegerField(u'FromPeriod:', validators=[InputRequired(), Length(max=2)])
    ToPeriod = SelectField(u'To Period', validators.InputRequired(),choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])