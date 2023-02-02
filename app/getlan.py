from flask import session
# ==============================================================================
# ==============================================================================
def galary_lang(galary): #Галарея
    content = []

    if session['lang'] == 'uz':
        for i in galary:
            content_items={'id' : i.id, 'image': i.photo}
            content.append(content_items)

    elif session['lang'] == 'ru':
        for i in galary:
            content_items={'id' : i.id, 'image': i.photo}
            content.append(content_items)

    else:
        for i in galary:
            content_items={'id' : i.id, 'image': i.photo}
            content.append(content_items)
    
    return content
# ==============================================================================
# ==============================================================================
def about_lang(about): #О нас
    # content = []
    content_items = {}

    if session['lang'] == 'uz':
        content_items={
            'id' : about.id, 'phone': about.phone, 
            'text' : about.text, 'email' : about.email,
            'instagram' : about.instagram,
            'telegram' : about.telegram,
            'youtube' : about.youtube, 'address' : about.address
            }
        # content.append(content_items)

    elif session['lang'] == 'ru':
        content_items={'id' : about.id, 'phone': about.phone, 
        'text' : about.ru_text, 'email' : about.email, 'instagram' : about.instagram,
        'telegram' : about.telegram, 'youtube' : about.youtube, 
        'address' : about.ru_address}
        # content.append(content_items)

    else:
        content_items={'id' : about.id, 'phone': about.phone, 
        'text' : about.en_text, 'email' : about.email, 'instagram' : about.instagram,
        'telegram' : about.telegram, 'youtube' : about.youtube, 
        'address' : about.en_address}
        # content.append(content_items)
    
    return content_items
# ==============================================================================
# ==============================================================================
def division_lang(division): #Отделения
    content = []

    if session['lang'] == 'uz':
        for i in division:
            result = {
            'name':i.name,
            'icon':i.svg_icon
            }
            content.append(result)

    elif session['lang'] == 'ru':
        for i in division:
            result = {
            'name':i.ru_name,
            'icon':i.svg_icon
            }
            content.append(result)

    else:
        for i in division:
            result = {
            'name':i.en_name,
            'icon':i.svg_icon
            }
            content.append(result)
    
    return content

# ==============================================================================
# ==============================================================================

def position_lang(position): #Должность
    content = []

    if session['lang'] == 'uz':
        for i in position:
            content.append(i.post)

    elif session['lang'] == 'ru':
        for i in position:
            content.append(i.ru_post)

    else:
        for i in position:
            content.append(i.en_post)

    return content

# ==============================================================================
# ==============================================================================

from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import Position


def personal_lang(personal): #Персонал
    content = []

    if session['lang'] == 'uz':
        for i in personal:

            position_name = Position.query.filter_by(id=i.position).first()
            post_name = None
            if position_name: post_name = position_name.post


            birth_date = relativedelta(datetime.today(), i.birth_date).years

            content_items={'id' : i.id, 'name': i.name, 
            'surname' : i.surname, 'fullname' : i.fullname, 'instagram' : i.instagram,
            'telegram' : i.telegram, 'number' : i.number, 'personal_id' : i.personal_id,
            'еxperience' : i.еxperience, 'birth_date' : birth_date, 'position':post_name,
            'image':i.image
            }
            content.append(content_items)

    elif session['lang'] == 'ru':
        for i in personal:

            position_name = Position.query.filter_by(id=i.position).first()
            post_name = None
            if position_name: post_name = position_name.ru_post
            birth_date = relativedelta(datetime.today(), i.birth_date).years

            content_items={'id' : i.id, 'name': i.ru_name, 
            'surname' : i.ru_surname, 'fullname' : i.ru_fullname, 'instagram' : i.instagram,
            'telegram' : i.telegram, 'number' : i.number, 'personal_id' : i.personal_id,
            'еxperience' : i.еxperience, 'birth_date' : birth_date, 'position':post_name,
            'image':i.image
            }
            content.append(content_items)

    else:
        for i in personal:

            position_name = Position.query.filter_by(id=i.position).first()
            post_name = None
            if position_name: post_name = position_name.en_post

            birth_date = relativedelta(datetime.today(), i.birth_date).years

            content_items={'id' : i.id, 'name': i.en_name, 
            'surname' : i.en_surname, 'fullname' : i.en_fullname, 'instagram' : i.instagram,
            'telegram' : i.telegram, 'number' : i.number, 'personal_id' : i.personal_id,
            'еxperience' : i.еxperience, 'birth_date' : birth_date, 'position':post_name,
            'image':i.image
            }
            content.append(content_items)
    
    return content

# ==============================================================================
# ==============================================================================

def art_lang(art): #Статья
    content = []

    if session['lang'] == 'uz':
        for i in art:
            content_items={'id' : i.id, 'photo': i.photo, 
            'youtube_link': i.youtube_link, 'text' : i.text, 
            'title' : i.title, 'created_date' : i.created_date,
            'updated_date' : i.updated_date
            }
            content.append(content_items)

    elif session['lang'] == 'ru':
        for i in art:
            content_items={'id' : i.id, 'photo': i.photo, 
            'youtube_link': i.youtube_link, 'text' : i.ru_text, 
            'title' : i.ru_title, 'created_date' : i.created_date,
            'updated_date' : i.updated_date
            }
            content.append(content_items)

    else:
        for i in art:
            content_items={'id' : i.id, 'photo': i.photo, 
            'youtube_link': i.youtube_link, 'text' : i.en_text, 
            'title' : i.en_title, 'created_date' : i.created_date,
            'updated_date' : i.updated_date
            }
            content.append(content_items)
    
    return content

# ==============================================================================
# ==============================================================================

def services_lang(services): #Услуги
    content = []

    if session['lang'] == 'uz':
        for i in services:
            content_items={'id' : i.id, 'name': i.name, 
            'description' : i.description, 'price' : i.price}
            content.append(content_items)

    elif session['lang'] == 'ru':
        for i in services:
            content_items={'id' : i.id, 'name': i.ru_name, 
            'description' : i.ru_description, 'price' : i.price}
            content.append(content_items)

    else:
        for i in services:
            content_items={'id' : i.id, 'name': i.en_name, 
            'description' : i.en_description, 'price' : i.price}
            content.append(content_items)
    
    return content