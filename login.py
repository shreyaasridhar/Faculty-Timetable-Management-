from flask_wtf import Form  
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, validators
from wtforms.validators import InputRequired, Length

class LoginForm(Form):
    username = StringField(u'User Name:', validators=[InputRequired(), Length(max=30)])
    passwd = PasswordField(u'Password:', validators=[Length(min=4, max=16)])