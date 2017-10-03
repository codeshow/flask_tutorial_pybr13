# coding: utf-8

import code
import click
from cms.app import create_app

app = create_app(__name__)


@click.group()
def main():
    """Flask CMS"""


@main.command()
def shell():
    """Abre um shell >>> com o `app` no contexto
    Se o ipython estiver instalado ira iniciar um shell Ipython
    Caso contrário iniciara um shell Python puro.
    """
    click.echo(f'Iniciando o shell do {app.config.SITENAME}')
    with app.app_context():
        try:
            from IPython import start_ipython
            start_ipython(argv=[], user_ns={'app': app})
        except:
            code.interact(banner=app.config.SITENAME, local={'app': app})


@main.command()
@click.option('--debug/--no-debug', default=app.config.DEBUG)
@click.option('--reloader/--no-reloader', default=app.config.RELOADER)
@click.option('--host', default=app.config.HOST)
@click.option('--port', default=app.config.PORT)
def runserver(debug, reloader, host, port):
    """Inicia o servidor em modo dev/debug"""
    app.run(debug=debug, use_reloader=reloader, host=host, port=port,
            extra_files=[f'{app.root_path}/settings.yml'])


@main.command()
@click.option('--username', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True,
              confirmation_prompt=True)
def adduser(username, password):
    """Cria um novo usuario"""
    with app.app_context():
        try:
            app.db.create_user(username, password)
        except Exception as e:
            click.echo(f'Nao foi possivel criar o usuario {username}')
            raise
        else:
            click.echo(f"Usuario {username} criado com sucesso!")


if __name__ == "__main__":
    main()
