from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, RadioField, StringField, BooleanField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired


class Fancy(FlaskForm):
    radio = RadioField(choices=[('yes','Да'),('no','Нет')])


class ArtForm(FlaskForm):
    meta_des = StringField('Meta des')
    meta_key = StringField('Meta key')

    photo = FileField(default='default.jpg')
    youtube = StringField('YouTube iframe')
    del_photo = BooleanField('Удалить фото')
    # filename = StringField('Названия папки', validators = [DataRequired()])

    title = StringField('Уз заголовок')
    ru_title = StringField('Ру заголовок')
    en_title = StringField('Анг заголовок')

    text = CKEditorField('Уз текст')
    ru_text = CKEditorField('Ру текст')
    en_text = CKEditorField('Анг текст')

    submit = SubmitField("Отправить")


class ServiceForm(FlaskForm):
    meta_des = StringField('Meta des')
    meta_key = StringField('Meta key')

    name = StringField('Название')
    ru_name = StringField('Ру название')
    en_name = StringField('Анг название')
    price = StringField('Цена')
    
    description = CKEditorField('Уз описание')
    ru_description = CKEditorField('Ру описание')
    en_description = CKEditorField('Анг описание')

    submit = SubmitField("Отправить")
