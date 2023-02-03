from flask import Blueprint

seo = Blueprint(
    'seo', __name__,
    template_folder='seo-templates',
    static_folder='seo-static'
)

from . import views
