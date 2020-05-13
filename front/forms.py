from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, DateTimeField
from wtforms import IntegerField, RadioField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name = StringField('Имя')
    surname = StringField('Фамилия')
    phone = StringField('Телефон')
    reason = StringField('Причина въезда')
    number = StringField('Телефон')
    date = DateTimeField('Дата')
    time = StringField('Время')
    submit = SubmitField('Подать заявку')