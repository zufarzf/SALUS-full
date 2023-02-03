from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Email

from wtforms import widgets, SelectMultipleField


class MetaForm(FlaskForm):
    keywords = TextAreaField()
    description = TextAreaField()
    submit = SubmitField()
