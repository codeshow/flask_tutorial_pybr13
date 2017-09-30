# 2) CLI (tudo começa na linha de comando)

```bash
cms/                   # module root
├── cli.py             # Ferramenta de linha de comando `cms --help`
```

Implementação de `cli.py`


```py
import code
import click

app = NotImplemented


@click.group()
def main():
    """Flask CMS"""


@main.command()
def shell():
    """Abre um shell >>> com o `app` no contexto"""
    with app.app_context():
        code.interact(banner='My Flask APP', local={'app': app})


@main.command()
@click.option('--debug/--no-debug', default=True)
@click.option('--reloader/--no-reloader', default=True)
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000)
def runserver(debug, reloader, host, port):
    """Inicia o servidor em modo dev/debug"""
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)


@main.command()
@click.option('--username', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True,
              confirmation_prompt=True)
def adduser(username, password):
    """Cria um novo usuário"""
    try:
        app.db.create_user(username, password)
    except Exception as e:
        click.echo(f'Não foi possivel criar o usuário {username}')
        raise
    else:
        click.echo(f"Usuário {username} criado com sucesso!")
```

E então:

```bash
$ cms
Usage: cms [OPTIONS] COMMAND [ARGS]...

  Flask CMS

Options:
  --help  Show this message and exit.

Commands:
  adduser    Cria um novo usuário
  runserver  Inicia o servidor em modo dev/debug
  shell      Abre um shell >>> com o `app` no contexto
```

e 

```bash
$ cms runserver --help
Usage: cms runserver [OPTIONS]

  Inicia o servidor em modo dev/debug

Options:
  --debug / --no-debug
  --reloader / --no-reloader
  --host TEXT
  --port INTEGER
  --help                      Show this message and exit.

```

Contudo repare o `app = NotImplemented` e como isso irá gerar os erros abaixo quando executarmos um comando:


```bash
$ cms runserver
...
AttributeError: 'NotImplementedType' object has no attribute 'run'
```


Precisamos implementar os factories que irão criar o `app` ex: `app = create_app`

