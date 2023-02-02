from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Email

from wtforms import widgets, SelectMultipleField

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class LoginForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min = 4, message="Loginni kiriting!")], render_kw={'placeholder' : 'Login...'})
    psw = PasswordField(validators=[DataRequired(), Length(min=4, max = 50, message="Parolni to'g'ri kiriting!")], render_kw={'placeholder' : 'Parol...'})
    remember = BooleanField(default=False)
    submit = SubmitField()

class ContactForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired(message="Вы не ввели имя!"),
            Length(min = 4, message="Имя и фамилия не должны быть короче 4 символов!")
            ])
    surname = StringField(
        validators=[
            DataRequired(message="Вы не ввели фамилию!"),
            Length(min = 4, message="Имя и фамилия не должны быть короче 4 символов!")
            ])
    phone_number = StringField(
        validators=[
            DataRequired(message="Вы не ввели номер телефона!"),
            Length(min = 9,max = 13, message="Номер телефона не должен быть короче 9 цифр!")
            ])
    telegram_address = StringField()
    message = TextAreaField(validators=[DataRequired(message="Вы не ввели сообщение!")])
    submit = SubmitField()
