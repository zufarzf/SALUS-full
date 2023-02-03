from flask import (
    render_template, session, redirect,
    flash, url_for
    )

from .. import db
from ..models import *
from .forms import MetaForm
from . import seo


@seo.route('/')
def seo_menu():
    if 'admin_login' in session and session['admin_login']:
        return render_template('seo_menu.html')
    else: return redirect(url_for('main.login'))




@seo.route('/menu_item/<menu_item>', methods=['GET', 'POST'])
def seo_form(menu_item):
    if 'admin_login' in session and session['admin_login']:

        pages_name = [
            'main', 'services', 'doctors', 'results', 'useful',
            'sign_up', 'contacts', 'sign_in', 'registration',
            'make_an_appointment']
        
        if menu_item in pages_name:

            form = MetaForm()

            keywords = ''
            description = ''
            meta_teg = MetaTags.query.filter_by(page_name=menu_item).first()
            if meta_teg:
                keywords = meta_teg.meta_keywords
                description = meta_teg.meta_description

            if form.validate_on_submit():
                if meta_teg == None:
                    meta_teg = MetaTags(
                        page_name=menu_item,
                        meta_keywords=form.keywords.data,
                        meta_description=form.description.data
                    )
                else:
                    meta_teg.meta_keywords=form.keywords.data
                    meta_teg.meta_description=form.description.data

                try:
                    db.session.add(meta_teg)
                    db.session.commit()
                    flash('Всё успешно сохранено!', category='valide-message')
                    return redirect(url_for('seo.seo_menu'))
                except:
                    flash('Ошибка при сохронении!\nПожалуйста повторите попытку.', category='invalide-message')
                    return redirect(url_for('seo.seo_form', menu_item=menu_item))

            return render_template(
                'seo_form.html',
                menu_item=menu_item,
                form=form,
                keywords = keywords,
                description = description,
                page_title='Редактировать мета данные'
                )
        else:
            flash('Ошибка!\nПожалуйста не меняйте ссылку меню!!!', category='invalide-message')
            return redirect(url_for('seo.seo_menu'))

    else: return redirect(url_for('main.login'))





@seo.route('/menu_item/about_seo_form', methods=['GET', 'POST'])
def about_seo_form():
    if 'admin_login' in session and session['admin_login']:

        form = MetaForm()

        keywords = ''
        description = ''
        meta_teg = About.query.first()
        if meta_teg:
            keywords = meta_teg.meta_keywords
            description = meta_teg.meta_description

        if form.validate_on_submit():
            if meta_teg:
                meta_teg.meta_keywords=form.keywords.data
                meta_teg.meta_description=form.description.data

            try:
                db.session.add(meta_teg)
                db.session.commit()
                flash('Всё успешно сохранено!', category='valide-message')
                return redirect(url_for('seo.seo_menu'))
            except:
                flash('Ошибка при сохронении!\nПожалуйста повторите попытку.', category='invalide-message')
                return redirect(url_for('seo.about_seo_form'))

        return render_template(
            'about_seo_form.html',
            form=form,
            keywords = keywords,
            description = description,
            page_title='Редактировать мета данные'
            )

    else: return redirect(url_for('main.login'))
