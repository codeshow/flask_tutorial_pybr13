from dynaconf.contrib.flask_dynaconf import FlaskDynaconf


def configure(app):
    """Configure Dynaconf Flask Extension
    Dynaconf permite que variaveis sejam carregadas de diversas fontes
    e arquivos diferentes.
    Como arquivos yaml, ini, json,
    bancos de dados como Mongo ou Redis
    e variavéis de ambiente
    """
    FlaskDynaconf(
        app=app,
        DYNACONF_NAMESPACE='CMS',
        SETTINGS_MODULE=f'{app.root_path}/settings.yml'
    )
