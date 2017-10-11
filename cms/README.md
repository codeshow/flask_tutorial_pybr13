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

Em nosso CMS iremos ler as configurações de um arquivo `cms/settings.yml` e também opcionalmente
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

Para começar a implentação do **config factory** no `cms/config/__init__.py`

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

E então invocaremos essa função no `app factory` em `cms/app/__init__.py`

> NOTA: repare que agora nosso `create_app` precisa receber `import_name` como parametro, isso acontece pois o import_name será importante para que ele consiga encontrar o arquivo de configuraçes, deixe o `cms/app/__init__.py` como o abaixo:

```py
from flask import Flask
from cms import config


def create_app(import_name='cms'):
    app = Flask(import_name)

    # Iniciar o sistema de configurações dinâmicas
    config.configure(app)

    return app

```

E no `cms/cli.py` passe o `__name__` como import_name para o `create_app`

```python
import code
import click
form cms.app import create_app

app = create_app(__name__)
...
```

e então ainda `cms/cli.py` podemos (opcionalmente) utilizar alguns valores default a partir do
`app.config`

Nas mensagens podemos fazer algo como:

```py
def shell(......):
    ...
    click.echo(f'Iniciando o shell do {app.config.SITENAME}')
    ...
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

> NOTA: veja a implementação do `cms/cli.py` nesta branch ali em cima se quiser dar um copy-paste :)

Pronto agora em qualquer momento podemos reescrever as configs no arquivo `settings.yml` ou exportar como variáveis de ambiente

```bash
export CMS_PORT='@int 3000'
export CMS_HOST='127.0.0.1'
export CMS_SITENAME='Meu Flask CMS!'
```

O próximo passo é carregar algumas extensões no `extension factory`


[<<-- anterior](../../../tree/cms_3_config_factory/cms)  -  [próximo -->>](../../../tree/cms_3_extension_factory/cms)

