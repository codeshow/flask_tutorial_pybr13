# coding: utf-8

from flask import Flask
from cms import config, ext


def create_app(import_name='cms'):
    """import_name tem que ser sempre a raiz do projeto
    onde está o cli.py, templates/ e static/"""

    app = Flask(import_name)

    # Iniciar o sistema de configurações dinâmicas
    config.configure(app)

    # Carregar as extensões
    ext.configure(app)

    return app
