from flask import (
    render_template, session, redirect,
    flash, url_for
    )

from .. import db
from ..models import *
from . import seo
from .forms import *


@seo.route('/', methods=['GET', 'POST'])
def seo_menu():
    if 'admin_login' in session and session['admin_login']:
        return render_template('seo_menu.html')
    else: return redirect(url_for('main.login'))
