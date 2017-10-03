# coding: utf-8

from flask import current_app
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash


def configure(app):
    """Inicializa o Flask Simple Login"""
    SimpleLogin(app, login_checker=login_checker)
    app.db.create_user = create_user

# Functions


def login_checker(user):
    """Valida o usuario e senha para efetuar o login"""
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False

    existing_user = current_app.db.users.find_one({'username': username})
    if not existing_user:
        return False

    if check_password_hash(existing_user.get('password'), password):
        return True

    return False


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if current_app.db.users.find_one({'username': username}):
        raise RuntimeError(f'{username} ja esta cadastrado')

    user = {'username': username,
            'password': generate_password_hash(password)}

    current_app.db.users.insert_one(user)
