# 1) Arquitetura do Projeto e dicas de estrutura e qualidade

Instalado através do `setup.py` com `python setup.py develop` e irá prover 
a ferramenta de linha de comando `cms` a partir da qual iremos rodar 
`cms runserver` e `cms shell` e `cms adduser`

A estrutura do projeto será:

```bash
Makefile               # Utilidades `install`, `clean`, `pep8` e `test`
setup.py               # Instalador do projeto `python setup.py develop`
tests/                 # Testes com py.test
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── config/            # Configuration Factory (Load de configurações)
├── ext/               # Extensões (Blueprints) do app
├── static/            # Arquivos estáticos (.css, .js, .images)
├── templates/         # Templates Jinja2
├── cli.py             # Ferramenta de linha de comando `cms --help`
├── __init__.py        # Python module init
├── README.md          # Este arquivo
└── settings.yml       # Configurações que serão carregadas
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

