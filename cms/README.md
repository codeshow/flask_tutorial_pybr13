# 3) Configuration factory

A estrutura do projeto será:

```bash
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── config/            # Configuration Factory (Load de configurações)
├── cli.py             # Ferramenta de linha de comando `cms --help`
└── settings.yml       # Configurações que serão carregadas
```

O Flask pode ler configurações de objetos, módulos Python e arquivos json
de acordo com o https://12factor.net/pt_br/config devemos ter configurações
default na aplicação mas todas as configurações variáveis deve ficar no ambiente.

Para isto usaremos a extensão `FlaskDynaconf` do módulo `dynaconf` com esta
extensão podemos ler as configurações a partir de arquivos, bancos de dados e 
variáveis de ambiente.

Em nosso CMS iremos ler as configurações de um arquivo `settings.yml` e também opcionalmente
de variáveis de ambiente.

```yaml
CMS:
  SECRET_KEY: 'real_secret_here'
  DB_NAME: cms_db
  SITENAME: Flask CMS
  HOST: '0.0.0.0'
  PORT: 5000
  DEBUG: true
  RELOADER: true
```

Para começar a implentação do **config factory** no `config/__init__.py`

```py
from dynaconf.contrib.flask_dynaconf import FlaskDynaconf


def configure(app):
    """Configure Dynaconf Flask Extension"""
    FlaskDynaconf(
        app=app,
        DYNACONF_NAMESPACE='CMS',
        SETTINGS_MODULE=f'{app.root_path}/settings.yml'
    )
```

E então invocaremos essa função no `app factory` em `app/__init__.py`

```py
from flask import Flask
from cms import config


def create_app():
    app = Flask(__name__)

    # Iniciar o sistema de configurações dinâmicas
    config.configure(app)

    return app

```

e então no `cli.py` podemos utilizar alguns valores default a partir do
`app.config`

Nas mensagens podemos fazer algo como:

```py
    click.echo(f'Iniciando o shell do {app.config.SITENAME}')
```

e também nas opções dos comandos.

```py
...
@click.option('--debug/--no-debug', default=app.config.DEBUG)
@click.option('--reloader/--no-reloader', default=app.config.RELOADER)
@click.option('--host', default=app.config.HOST)
@click.option('--port', default=app.config.PORT)
def runserver(debug, reloader, host, port):
...
```

Pronto agora em qualquer momento podemos reescrever as configs no arquivo `settings.yml` ou exportar como variáveis de ambiente

```bash
export CMS_PORT='@int 3000'
export CMS_HOST='127.0.0.1'
export CMS_SITENAME='Meu Flask CMS!'
```

O próximo passo é carregar algumas extensões no `extension factory`
