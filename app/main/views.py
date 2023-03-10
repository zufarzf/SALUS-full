from flask import render_template, redirect, url_for, flash, session, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from . import main
from .UserLogin import UserLogin
from .. import manager
from ..models import *
from ..getlan import *
from .forms import *

from telegram_send import send




@manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id)

# ==============================================================================
# ==============================================================================
@main.route('/') # Главня страница
def main_page():
    #  ============= FOR CRUD ITEMS IN SERVICES AND ART =============
    session['item_id'] = None
    session['del_id'] = None
    session['seritem_id'] = None
    session['serdel_id'] = None

    # ============= ============= =============
    if 'lang' not in session:
        session['lang'] = 'ru'
    #--------- Unique admin ----------
    count = 0
    has_admin = Users.query.filter_by(is_admin=True).all()
    psw = 'pbkdf2:sha256:260000$dQbsDghczwZkOmPf$3bc745a245ed6f351fb38fced22d3c25025f8bb7c21253f6f8996633c379d978'

    if len(has_admin) == 0:
        user = Users(name='usadmin', psw=psw, is_admin=True)
        db.session.add(user)
        db.session.commit()
    else:
        for person in has_admin:
            if person.name == 'usadmin' and person.psw == psw:
                count = 0
                break
            else:
                count += 1
        if count >= 1 :
            user = Users(name='usadmin', psw=psw, is_admin=True)
            db.session.add(user)
            db.session.commit()


    # ------- end of the unique admin --------

    if 'lang' not in session:
        session['lang'] = 'uz'

    # # ---------------------------------

    division = Division.query.all()
    personal = Personal.query.all()
    about = About.query.first()
    art = Art.query.order_by(Art.created_date.desc()).limit(4).all()


    # # ---------------------------------

    division = division_lang(division)
    personal = personal_lang(personal)
    
    if about: about = about_lang(about)
    else: about = ''
    art_left = []
    if art_lang(art): art_left = art_lang(art)[0:3]
    art_right = {}
    if art_lang(art): art_right = art_lang(art)[3]

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='main').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template("main.html", 
                            division = division,
                            personal = personal, 
                            art_left = art_left,
                            art_right = art_right,
                            about = about,
                            page_title="SALUS",
                            keywords=keywords,
                            description=description
                            )



# ====== Все услуги ======
@main.route('/services/')
def services():
    if 'lang' not in session:
        session['lang'] = 'ru'
    # # ---------------------------------
    division_db = Division.query.all()
    division = division_lang(division_db)
    # # ---------------------------------

    result = dict()
    for i in division:
        if session['lang'] == 'uz':
            dev_id = Division.query.filter_by(name=i['name']).first()
            services = Services.query.filter_by(division=dev_id.id).all()
            result[i['name']] = services_lang(services)

        if session['lang'] == 'ru':
            div = Division.query.filter_by(ru_name=i['name']).first()
            name = div.id

            services = Services.query.filter_by(division=name).all()
            result[i['name']] = services_lang(services)

        if session['lang'] == 'en':
            div = Division.query.filter_by(en_name=i['name']).first()
            name = div.id

            services = Services.query.filter_by(division=name).all()
            result[i['name']] = services_lang(services)
    

    if session['lang'] == 'uz': page_title = 'Xizmatlar'
    elif session['lang'] == 'ru': page_title = 'Услуги'
    else: page_title = 'Services'

    ''' return -> { 'Хирургия' : [
                                    {'id': 1, 'name' : 'lorem'....},
                                    {'id': 1, 'name' : 'lorem ipsum'....}
                                    ],

                    'УЗИ' : [
                            {'id': 1, 'name' : 'lorem'....},
                            {'id': 1, 'name' : 'lorem'....}
                            ]
                        
                        !!! KEY - Отделения, VALUE - сервисы '''

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='services').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

        
    return render_template(
        'services.html',
        services=result,
        page_title=page_title,
        division=division,
        keywords=keywords,
        description=description
        )


# Подробно об услуги 
@main.route('/services/<int:service_id>')
def service_item(service_id):
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    item = Services.query.filter_by(id = service_id).all()
    result = services_lang(item)
    # ----- ----- -----

    if item:
        division_id = item[0].division

        # ----- ----- -----
        personal = Personal.query.filter_by(division=division_id).all()
        personal = personal_lang(personal)  
    else:
        item = []
    # ----- ----- -----  
    
    keywords=''
    description=''
    # -------------------------------------
    if item[0]:
        keywords=item[0].meta_keywords
        description=item[0].meta_description


    return render_template('in_page-service.html',
                            item=result,
                            personal=personal,
                            keywords=keywords,
                            description=description
                            )


# ====== Врачи ======
@main.route('/doctors')
def doctors():
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    doctors = Personal.query.filter_by(is_doctor=True).all()
    if doctors:
        doctors = personal_lang(doctors) 
    else:
        doctors = [] 
    # ----- ----- -----  

    if session['lang'] == 'uz': page_title = 'Shifokorlar'
    elif session['lang'] == 'ru': page_title = 'Врачи'
    else: page_title = 'Doctors'

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='doctors').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template(
        'doctors.html',
        doctors=doctors,
        page_title=page_title,
        keywords=keywords,
        description=description
        )


# ====== Статьи ======
@main.route('/arts')
def arts():
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    art = Art.query.order_by(Art.created_date.desc()).all()
    if art:
        art = art_lang(art)  
    else:
        art=[]
    # ----- ----- -----  

    if session['lang'] == 'uz': page_title = 'Foydali'
    elif session['lang'] == 'ru': page_title = 'Полезное'
    else: page_title = 'Usefuls'

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='useful').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template(
        'useful.html', arts=art,
        page_title=page_title,
        keywords=keywords,
        description=description
        )


# Подробно о статьях 
@main.route('/arts/<int:arts_id>')
def arts_item(arts_id):
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    art_item_db = Art.query.filter_by(id=arts_id).all()
    if art_item_db: art_item = art_lang(art_item_db) 
    else: art_item=[]
    # ----- ----- -----  

    keywords=''
    description=''
    # -------------------------------------
    if art_item_db[0]:
        keywords=art_item_db[0].meta_keywords
        description=art_item_db[0].meta_description

    return render_template(
        'in_page-useful.html',
        art_item=art_item,
        keywords=keywords,
        description=description
        )


# ====== О нас ======
@main.route('/about')
def about():
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    about_db = About.query.first()
    # ----- ----- -----  
    if about_db: about = about_lang(about_db)  
    else: about = None
    # ----- ----- -----  
    galary = Galary.query.all()
    # if galary: galary = galary_lang(galary)
    # else: galary = []
    # ----- ----- ----- 


    if session['lang'] == 'uz': page_title = 'Biz haqimizda'
    elif session['lang'] == 'ru': page_title = 'О нас'
    else: page_title = 'About'

    keywords=''
    description=''
    # -------------------------------------
    if about_db:
        keywords=about_db.meta_keywords
        description=about_db.meta_description

    return render_template('about.html', 
                            about=about,galary=galary,
                            page_title=page_title,
                            keywords=keywords,
                            description=description)




# ====== Контакты ======
@main.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if 'lang' not in session:
        session['lang'] = 'ru'
    # ----- ----- -----
    contacts = About.query.first()
    if contacts:
        contacts = about_lang(contacts)  
    else:
        contacts = []
    # ----- ----- -----

    form = ContactForm()
    if form.validate_on_submit():
        try:
            send(
                messages = [
                    f'''
Имя: {form.name.data}
Фамилия: {form.surname.data}
Номер телефона: {form.phone_number.data}
Телегоамм: {form.telegram_address.data}

----------------------------------------

Сообщение:

{form.message.data}
                    '''
                ]
            )
            flash('Сообщение успешно отправлено!', category='valide-message')
            return redirect(url_for('main.contacts'))
        except:
            flash('Ошибка при отправке! Пожалуйста, повторите попытку.', category='invalide-message')
            return redirect(url_for('main.contacts'))



    if session['lang'] == 'uz': page_title = 'Aloqa'
    elif session['lang'] == 'ru': page_title = 'Контакты'
    else: page_title = 'Contact'


    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='contacts').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template(
                            'contacts.html',
                            contacts=contacts,
                            page_title=page_title,
                            form=form,
                            keywords=keywords,
                            description=description)





@main.route('/lang/<lang_code>/<site_path>')  # Меняет язык
def lang(lang_code,site_path):
    if 'lang' not in session:
        session['lang'] = 'ru'
    else: session['lang'] = lang_code
    return redirect(url_for(site_path))





# ==== login part ====
@main.route("/login/", methods=['POST', 'GET'])
def login():
    if 'lang' not in session:
        session['lang'] = 'ru'
    if current_user.get_id():
        idp = current_user.get_id()
        us = Users.query.filter_by(id=idp).first()
        if current_user.is_authenticated and us.is_admin:
            return redirect(url_for('admin.index'))


    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        psw = form.psw.data

        user = Users.query.filter_by(name=name).first()

        if user:
            if check_password_hash(user.psw, psw):
                userlogin = UserLogin().create(user)
                rm = True if form.remember.data else False
                login_user(userlogin, remember=rm)
                if user.is_admin: session['admin_login'] = True
                session['user_login'] = user.id
                return redirect(url_for('admin.index'))
            else:
                if session['lang'] == 'uz':
                    flash("Noto'g'ri login yoki parol!", category='invalide-message')
                if session['lang'] == 'ru':
                    flash("Неправильный логин или пароль!", category='invalide-message')
                else: flash("Incorrect login or password!", category='invalide-message')
                return redirect(url_for('main.main_page'))
        else: 
            if session['lang'] == 'uz':
                flash("Noto'g'ri login yoki parol!", category='invalide-message')
            if session['lang'] == 'ru':
                flash("Неправильный логин или пароль!", category='invalide-message')
            else: flash("Incorrect login or password!", category='invalide-message')

    if session['lang'] == 'uz': page_title = 'Kirish'
    elif session['lang'] == 'ru': page_title = 'Вход'
    else: page_title = 'Sign in'

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='sign_in').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template(
                            'sign_in.html', form=form,
                            page_title=page_title,
                            keywords=keywords,
                            description=description)




@main.route('/logout')
def logout():
    logout_user()
    del session['admin_login']
    del session['user_login']
    return redirect(url_for('main.main_page'))



# ========== for admin dashboard ===========
@main.route('/session_add/<int:item_id>')
@login_required
def artsession_add(item_id):
    session['item_id'] = item_id

    return redirect(url_for('editart_block.editart'))


@main.route('/delete/<int:item_id>', methods=['POST', 'GET'])
@login_required
def artdelete(item_id):
    
    session['del_id'] = item_id
        
    return redirect(url_for('artdelete_block.artdelete'))

# for service block
@main.route('/sersession_add/<int:item_id>')
@login_required
def sersession_add(item_id):
    session['seritem_id'] = item_id

    return redirect(url_for('editser_block.editser'))


@main.route('/serdelete/<int:item_id>', methods=['POST', 'GET'])
@login_required
def serdelete(item_id):
    session['serdel_id'] = item_id
    print(session['serdel_id'])
    return redirect(url_for('serdelete_block.serdelete'))






@main.route('/make_an_appointment')
def make_an_appointment():
    if 'lang' not in session:
        session['lang'] = 'ru'

    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='make_an_appointment').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description

    return render_template(
        'make_an_appointment.html',
        keywords=keywords,
        description=description)



@main.route('/results')
def results():
    if 'lang' not in session:
        session['lang'] = 'ru'


    keywords=''
    description=''
    # -------------------------------------
    meta_tags = MetaTags.query.filter_by(page_name='results').first()
    if meta_tags:
        keywords=meta_tags.meta_keywords
        description=meta_tags.meta_description
    return render_template(
        'results.html',
        keywords=keywords,
        description=description)
