# coding: utf-8

from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required

# decorate Flask-Admin view via Monkey Patching
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)


def configure(app):
    """Inicia uma instancia do Flask-Admin"""
    app.admin = Admin(
        app,
        name=app.config.get('FLASK_ADMIN_NAME', 'Flask CMS'),
        template_mode=app.config.get('FLASK_ADMIN_TEMPLATE_MODE', 'bootstrap3')
    )
