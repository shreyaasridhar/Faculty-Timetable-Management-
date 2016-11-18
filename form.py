from flask_wtf import Form  
from wtforms import StringField, BooleanField, TextAreaField, validators,IntegerField,SelectField
from wtforms.validators import InputRequired, Length

class SwapForm(Form):
    FromDay = SelectField(u'To Period', choices = [('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')])
    ToDay = SelectField(u'To Period', choices = [('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')])
    FromPeriod = SelectField(u'To Period', choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])
    ToPeriod = SelectField(u'To Period', choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])