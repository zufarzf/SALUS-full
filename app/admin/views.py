
from flask import abort, Markup, url_for, session, request, current_app, g, redirect, flash
from flask_admin import Admin, AdminIndexView, expose, form, BaseView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from wtforms import validators

import os
from random import random
from uuid import uuid4
from datetime import datetime


from app.admin import admin_panel
# from app.main.views import arr
from app.models import *
from app import app, db
from app.admin.form import *


file_path=os.path.abspath(os.path.dirname(__name__))
STORAGE = os.path.join(file_path, 'app/main/main-static/file/')

def name_gen_image(model, file_data):
    hash_name = f'{str(uuid4())}.png'
    return hash_name

def title_gen_file(model, file_data):
    hash_name = f'{str(uuid4())}'
    return hash_name

def title_gen_image(model, file_data):
    hash_name = f'{str(uuid4())}'
    return hash_name


class DashboardView(AdminIndexView):
    @expose('/')
    def index(self, *func):
        if current_user.get_id():
            self.idp = current_user.get_id()
            us = Users.query.filter_by(id=self.idp).first()
            if current_user.is_authenticated and us.is_admin:

                return self.render('index.html')
        else:
            raise abort(404)

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

admins = Admin(app, name='The Admin dashboard of the clinic Salus', template_mode='bootstrap3', index_view=DashboardView())


class AboutView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_labels = {
        'id' : 'ID',
        'text' : 'Уз Текст',
        'ru_text' : 'Ру текст',
        'en_text' : 'Анг текст',
        'address' : 'Уз адрес',
        'ru_address' : 'Ру адрес',
        'en_address' : 'Анг адрес',
        'phone' : 'Телефон',
        'instagram' : 'Instagram ссылка',
        'telegram' : 'Telegram ссылка',
        'youtube' : 'Youtube ссылка',
    }
    
    can_export = True
    # create_modal = True
    # edit_modal = True


class DivisionView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_labels = {
        'id' : 'ID',
        'name' : 'Название',
        'ru name' : 'Ру название',
        'en name' : 'Анг название',
        'personal' : 'Персонал',
        'services' : 'Услуги',
    }
    
    can_export = True
    # create_modal = True
    # edit_modal = True


class PositionView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_labels = {
        'id' : 'ID',
        'post' : 'Название',
        'ru_post' : 'Ру название',
        'en_post' : 'Анг название',
        'personal' : 'Персонал',
    }
    
    can_export = True
    # create_modal = True
    # edit_modal = True


class GalaryView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


    column_labels = {
        'id' : 'ID',
        'image' : 'Фото',
    }
    # can_export = True
    # create_modal = True
    # edit_modal = True 

    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''

        # url = 'main/main-static/storage/user_img/'+ model.image
        url = url_for('main.static', filename=os.path.join('static_files/about_images/', model.image))

        if model.image.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')


    form_extra_fields = {
        "image" : form.ImageUploadField('Аватарка', base_path=os.path.join(file_path, 'app/main/main-static/static_files/about_images/'),
                                        url_relative_path='app/main/main-static/static_files/about_images/', namegen=name_gen_image,
                                        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'gif'], max_size=(1200, 780, True),
                                        thumbnail_size=(100, 100, True),)}

    column_formatters = {
        'image':_list_thumbnail
    }

    def create_form(self, obj=None):
        return super(GalaryView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(GalaryView, self).edit_form(obj)



class PersonalView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_labels = {
        'id' : 'ID',
        'name' : 'Уз имя',
        'ru_name' : 'Ру имя',
        'en_name' : 'Анг имя',
        'surname' : 'Уз фамилия',
        'ru_surname' : 'Ру фамилия',
        'en_surname' : 'Анг фамилия',
        'fullname' : 'Уз отчество',
        'ru_fullname' : 'Ру отчество',
        'en_fullname' : 'Анг отчество',
        'personal_id' : 'ID персонала',
        'number' : 'Телефон',
        'telegram' : 'Telegram ссылка',
        'instagram' : 'Instagram ссылка',
        'еxperience' : 'Опыт',
        'birth_date' : 'Дата рождения',
        'created_date' : 'Дата создания',
        'updated_date' : 'Дата изменения',
        'login' : 'Login лич.каб',
        'psw' : 'Пароль лич.каб',
        'is_doctor' : 'Доктор',
        'art' : 'Статья', 
        'image' : 'Фото', 
    }
    
    can_export = True
    # create_modal = True
    # edit_modal = True
    def _list_thumbnail(view, context, model, name):
                if not model.image:
                    return ''

                # url = 'main/main-static/storage/user_img/'+ model.image
                url = url_for('main.static', filename=os.path.join('static_files/doctors_photos/', model.image))

                if model.image.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
                    return Markup(f'<img src={url} width="100">')


    form_extra_fields = {
        "image" : form.ImageUploadField('Фото', base_path=os.path.join(file_path, 'app/main/main-static/static_files/doctors_photos/'),
                                        url_relative_path='app/main/main-static/static_files/doctors_photos/', namegen=name_gen_image,
                                        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'gif'], max_size=(1200, 780, True),
                                        thumbnail_size=(100, 100, True),)}

    column_formatters = {
        'image':_list_thumbnail
    }

    def create_form(self, obj=None):
        return super(PersonalView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(PersonalView, self).edit_form(obj)


class UsersView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


    column_labels = {
        'id' : 'ID',
        'name' : 'Логин',
        'psw' : 'Пароль',
        'is_admin' : 'Админ',
    }

    form_args = {
        'name':dict(validators=[validators.DataRequired()]),
        'psw':dict(validators=[validators.DataRequired()])
    }

    def on_model_change(self, view, model, is_created):
        model.psw = generate_password_hash(model.psw)

    column_hide_backrefs = False
    column_list = ('name', 'psw', 'is_admin')
    can_export = True
    create_modal = True
    edit_modal = True



# ====================== ART BLOCK ======================

class ArtView(BaseView):
    @expose('/')
    def art(self, *func):
        arts = Art.query.all()
        # form = ArtForm()


        return self.render('art.html', arts = arts)
        

# ========================= ============================

class AddArtView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    # @csrf.exempt
    def addart(self):
        addform = ArtForm()
        
        if addform.validate_on_submit():

            m_des = addform.meta_des.data
            m_key = addform.meta_key.data
            photo = addform.photo.data
            youtube = addform.youtube.data
            title = addform.title.data
            ru_title = addform.ru_title.data
            en_title = addform.en_title.data
            text = addform.text.data
            ru_text = addform.ru_text.data
            en_text = addform.en_text.data
            # file = addform.filename.data
       

            # ------------ ------------- -------------
            if photo != 'default.jpg':
                filename = str(uuid4()) + '.' + photo.filename.split('.')[-1]
                photo.save(os.path.join('app/main/', f'main-static/static_files/useful/usefuls-images/', filename))
                photo=filename
            else:
                photo = 'app/admin/admin-static/default/default.jpg'

                # if filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg') or filename.endswith('jfif'):
                    
                #     newpath = f'app/admin/admin-static/uploads/{file}/' 
                #     if not os.path.exists(newpath):
                #         os.makedirs(newpath)

                #     photo.save(os.path.join('app/admin/', f'admin-static/uploads/{file}/', filename))
                
                # photo=filename
            
            # ------------ ------------- -------------

            result = Art(meta_description=m_des,
                        meta_keywords=m_key, photo=photo,
                        youtube_link=youtube, title=title,
                        ru_title=ru_title, en_title=en_title,
                        text=text, ru_text=ru_text,
                        en_text=en_text)

            db.session.add(result)
            db.session.commit()

            flash("Запись успешно записан!")

            return redirect(url_for('art_block.art'))

        return self.render('add_art.html',
                            addform = addform)


# ========================= ============================

class EditView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    def editart(self):
        if session['item_id'] == None:
            return redirect(url_for('art_block.art'))

        form = ArtForm()

        item_id = session['item_id']
        items = Art.query.filter_by(id=item_id).first()
        
        
        if form.validate_on_submit():
            items.meta_description = form.meta_des.data
            items.meta_keywords = form.meta_key.data
            photo = form.photo.data
            items.youtube_link = form.youtube.data
            items.title = form.title.data
            items.ru_title = form.ru_title.data
            items.en_title = form.en_title.data
            items.text = form.text.data
            items.ru_text = form.ru_text.data
            items.en_text = form.en_text.data
            items.del_photo = form.del_photo.data
            # items.filename = form.filename.data
            
            if photo:
                # --------------- --------------- ---------------
                if photo != 'default.jpg':
                    filename = str(uuid4()) + '.' + photo.filename.split('.')[-1]
                    filename = secure_filename(filename)
                else:
                    filename = 'app/admin/admin-static/default/default.jpg'
                # --------------- --------------- ---------------

                if filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg') or filename.endswith('jfif'):

                    if items.photo and items.photo != 'app/admin/admin-static/default/default.jpg' and filename != 'app/admin/admin-static/default/default.jpg':
                        os.remove('app/main/main-static/static_files/useful/usefuls-images/' + items.photo)
                        photo.save(os.path.join('app/main/', 'main-static/static_files/useful/usefuls-images/', filename))
                        items.photo=filename
                    # --------------- --------------- ---------------
                    elif items.photo == 'app/admin/admin-static/default/default.jpg' and form.photo.data != 'default.jpg':
                        photo.save(os.path.join('app/main/', 'main-static/static_files/useful/usefuls-images/', filename))
                        items.photo=filename
                    # --------------- --------------- ---------------
                    elif items.photo == 'app/admin/admin-static/default/default.jpg' and form.photo.data == 'default.jpg':
                        items.photo = 'app/admin/admin-static/default/default.jpg'
                    # --------------- --------------- ---------------
                    elif form.del_photo.data == True:
                        os.remove(f'app/main/main-static/static_files/useful/usefuls-images/' + items.photo)
                        items.photo = 'app/admin/admin-static/default/default.jpg'
                    

                    # ========== PAPKA BILAN SORTIROVKA BOLYATGANDAGI KOD ===========

                    # newpath = f'app/admin/admin-static/uploads/{form.filename.data}/' 
                    # another = f'{form.filename.data}{uuid4()}'
                    # another_newpath = f'app/admin/admin-static/uploads/{another}/' 

                    # if items.filename and items.filename != form.filename.data:
                    #     os.rename(f"app/admin/admin-static/uploads/{items.filename}/", newpath)

                    # elif not os.path.exists(newpath) and not items.filename and not items.photo:
                    #     os.makedirs(newpath)
                    #     photo.save(os.path.join('app/admin/', f'admin-static/uploads/{form.filename.data}/', filename))

                    # elif os.path.exists(newpath) and items.filename and items.filename != form.filename.data:
                    #     os.makedirs(another_newpath)
                    #     photo.save(os.path.join('app/admin/', f'admin-static/uploads/{another}/', filename))
                    #     items.filename = another

                    # elif items.filename == form.filename.data and os.path.exists(newpath):
                    #     if items.photo:
                    #         os.remove(f'app/admin/admin-static/uploads/{items.filename}/' + items.photo)
                    #     photo.save(os.path.join('app/admin/', f'admin-static/uploads/{form.filename.data}/', filename))   
                
            
            updated_date = datetime.utcnow()
            items.updated_date = updated_date

            db.session.add(items)
            db.session.commit()
            session['item_id'] = None
            
            return redirect(url_for("art_block.art"))
        
        return self.render('artedit.html', items = items, form=form)


# ========================= ============================

class DeleteView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    def artdelete(self, *func):
        if session['del_id'] == None:
            return redirect(url_for('art_block.art'))
        form = Fancy()

        if form.validate_on_submit():
            result = form.radio.data

            if result == 'yes':
                
                item = Art.query.filter_by(id=session['del_id']).first()
                if item.photo == 'default.jpg':
                    item = Art.query.filter_by(id=session['del_id']).delete()
                else:
                    item_obj = Art.query.filter_by(id=session['del_id']).first()

                    if item_obj.photo != 'app/admin/admin-static/default/default.jpg':
                        os.remove(f'app/main/main-static/static_files/useful/usefuls-images/' + item_obj.photo)
                    
                    item = Art.query.filter_by(id=session['del_id']).delete()

                
                session['del_id']=None

                return redirect(url_for('art_block.art'))
            elif result == 'no':
                return redirect(url_for('art_block.art'))
        
        return self.render('artdelete.html', form=form)


# ====================== END OF THE ART BLOCK ====================== 


# ====================== SERVICE BLOCK ======================

class ServiceView(BaseView):
    @expose('/')
    def service(self, *func):
        service = Services.query.all()
        form = ServiceForm()

        return self.render('service.html', service = service, form=form)


# ========================= ============================

class AddServiceView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    # @csrf.exempt
    def addservice(self):
        addform = ServiceForm()
        
        if addform.validate_on_submit():

            m_des = addform.meta_des.data
            m_key = addform.meta_key.data
            name = addform.name.data
            ru_name = addform.ru_name.data
            en_name = addform.en_name.data
            price = addform.price.data
            desc = addform.description.data
            ru_desc = addform.ru_description.data
            en_desc = addform.en_description.data
        
            # ------------ ------------- -------------
            
            result = Services(meta_description=m_des,
                        meta_keywords=m_key, name=name,
                        ru_name=ru_name, en_name=en_name,
                        description=desc, ru_description=ru_desc,
                        en_description=en_desc, price=price)

            db.session.add(result)
            db.session.commit()

            flash("Запись успешно записан!")

            return redirect(url_for('service_block.service'))

        return self.render('add_service.html',
                            addform = addform)


# ========================= ============================

class EditSerView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    def editser(self):
        if session['seritem_id'] == None:
            return redirect(url_for('service_block.service'))

        form = ServiceForm()

        item_id = session['seritem_id']
    
        items = Services.query.filter_by(id=item_id).first()
        
        
        if form.validate_on_submit():
            items.meta_description = form.meta_des.data
            items.meta_keywords = form.meta_key.data
            items.name = form.name.data
            items.ru_name = form.ru_name.data
            items.en_name = form.en_name.data
            items.description = form.description.data
            items.ru_description = form.ru_description.data
            items.en_description = form.en_description.data
            items.price = form.price.data
                
            
            updated_date = datetime.utcnow()
            items.updated_date = updated_date

            db.session.add(items)
            db.session.commit()

            session['seritem_id'] = None
            
            return redirect(url_for("service_block.service"))
        
        return self.render('seredit.html', items = items, form=form)


# ========================= ============================

class DeleteSerView(BaseView):
    @expose('/', methods=['POST', 'GET'])
    def serdelete(self, *func):
        if session['serdel_id'] == None:
            return redirect(url_for('service_block.service'))
        form = Fancy()

        if form.validate_on_submit():
            result = form.radio.data

            if result == 'yes':
                Services.query.filter_by(id=session['serdel_id']).delete()
                
                session['serdel_id']=None
                return redirect(url_for('service_block.service'))
            elif result == 'no':
                return redirect(url_for('service_block.service'))
        
        

        return self.render('artserdelete.html', form=form)

# ====================== END OF THE SERVICE BLOCK ======================


admins.add_view(DivisionView(Division, db.session, 'Отделения'))
admins.add_view(PositionView(Position, db.session, 'Должность'))
admins.add_view(AboutView(About, db.session, 'О нас'))
admins.add_view(GalaryView(Galary, db.session, 'Галарея'))
admins.add_view(PersonalView(Personal, db.session, 'Персонал'))
admins.add_view(UsersView(Users, db.session, 'Админы'))
# -----------------------------------------------------
admins.add_view(ArtView(name='Статьи', endpoint='art_block'))
admins.add_view(AddArtView(name='Добавить статью', endpoint='addart_block'))
admins.add_view(EditView(name='Изменить статью', endpoint='editart_block'))
admins.add_view(DeleteView(name='Удалить статью', endpoint='artdelete_block'))
# -----------------------------------------------------
admins.add_view(ServiceView(name='Услуги', endpoint='service_block'))
admins.add_view(AddServiceView(name='Добавить услугу', endpoint='addser_block'))
admins.add_view(EditSerView(name='Изменить услугу', endpoint='editser_block'))
admins.add_view(DeleteSerView(name='Удалить услугу', endpoint='serdelete_block'))