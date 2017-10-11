# 3) Extension Factory

```bash
tests/                 # Testes com py.test
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── ext/               # Extensões (Blueprints) do app
└── settings.yml       # Configurações que serão carregadas
```

Hora de carregar as extensões que usaremos no projeto sendo elas:

- **TinyMongo** - Banco de dados NoSQL baseado em arquivos json
- **Flask Admin** - Interface administrativa
- **Flask SimpleLogin** - Autenticação
- **Flask Debug Toolbar** - Ferramenta para debug

Para carregar essas extensões usaremos o conceito de `extension factory` e de
forma dinâmica carregamos as extensões que serão definidas no `cms/settings.yml`

Vamos começar inicializando as extensões básicas e depois customizaremos o 
`admin` e a parte de `autenticação`

No `cms/settings.yml` adicionaremos o item `EXTENSIONS`

```py
CMS:
  SECRET_KEY: 'real_secret_here'
  DB_NAME: cms_db
  SITENAME: Flask CMS
  HOST: '0.0.0.0'
  PORT: 5000
  DEBUG: true
  RELOADER: true

  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure

```

Carregaremos dinamicamente todos os módulos definidos na lista `EXTENSIONS` e
para cada um esperamos a existencia de uma função `configure` que recebe `app`
como único argumento.

a primeira coisa a fazer é implementar o `extension factory` em `cms/ext/__init__.py` utilizando o `import_string` para a partir de um texto contento o caminho completo de um módulo podermos importa-lo para um objeto Python como na implementação abaixo: 

Implemente em `cms/ext/__init__.py`

```py
import import_string


def configure(app):
    """Extension Factory, carrega as extensões definidas em
    app.config.EXTENSIONS
    """
    for extension in app.config.get('EXTENSIONS', []):
        try:
            factory = import_string(extension)
            factory(app)
        except Exception as e:
            app.logger.error(f'Erro ao carregar {extension}: {e}')
        else:
            app.logger.info(f'Extensão {extension} carregada com sucesso!')

```

Agora é só invocar este factory no `cms/app/__init__.py` app factory `create_app`

```py
from flask import Flask
from cms import config, ext


def create_app(import_name):
    """import_name tem que ser sempre a raiz do projeto
    onde está o cli.py, templates/ e static/"""

    app = Flask(import_name)

    # Iniciar o sistema de configurações dinâmicas
    config.configure(app)

    # Carregar as extensões
    ext.configure(app)         #   < --- Extension Factory iniciado aqui

    return app
```

# Extensões

A primeira extensão que carregamos é a de banco de dados e neste tutorial estamos usando o `TinyDB` com `TinyMongo` pois este banco de dados não exige a instalação do MongoDB, oferece as mesmas funcionalidades porém salvando os dados em um simples arquivo JSON.

> NOTA: Em produção você poderá trocar para uma conexão com o `MongoClient` o TinyDB é apenas para desenvolvimento.

## TinyMongo

Implemente `cms/ext/database.py` (crie esse novo arquivo)

```py
from pathlib import Path
from tinymongo import TinyMongoClient

def configure(app):
    """Inicia o client do TinyMongo e adiciona `app.db`
    *para usar MongoDB basta mudar para `pymongo.MongoClient`
    """
    db_folder = app.config.get('DB_FOLDER', 'database')
    db_name = app.config.get('DB_NAME', 'cms_db')
    foldername = Path(db_folder) / Path(app.root_path) / Path('database')
    client = TinyMongoClient(foldername=foldername)
    app.db = client[db_name]
```

> NOTA: uma atenção especial a linha `app.db = client[db_name]` pois nela estamos fazendo a atribuição de nossa referencia a um banco de dados para um atributo do **app** e isso funciona bem em alguns casos como o TinyDB, porém para casos como **SQLAlchemy** é mais recomendado atribuir o objeto **db** ao Flask Global Object `from flask import g; g.db = client[db_name]` pois este objeto tem escopo global apenas durante o request.

## Autenticação

Para autenticação usaremos o `Flask_simplelogin` que é a extensão mais simples para login no Flask.

Implemente um novo arquivo `cms/ext/auth.py`

```py
from flask import current_app
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash


def configure(app):
    """Inicializa o Flask Simple Login"""
    SimpleLogin(app, login_checker=login_checker)
    app.db.create_user = create_user

# Functions


def login_checker(user):
    """Valida o usuário e senha para efetuar o login"""
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
    """Registra um novo usuário caso não esteja cadastrado"""
    if current_app.db.users.find_one({'username': username}):
        raise RuntimeError(f'{username} já está cadastrado')

    user = {'username': username,
            'password': generate_password_hash(password)}

    current_app.db.users.insert_one(user)

```

## Interface admin 

IMplemente o novo arquivo `cms/ext/admin.py`

```py
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required

# decorate Flask-Admin views for login via Monkey Patching
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

def configure(app):
    """Inicia uma instância do Flask-Admin"""
    app.admin = Admin(
        app,
        name=app.config.get('ADMIN_NAME', 'Flask CMS'),
        template_mode=app.config.get('ADMIN_STYLE', 'bootstrap3')
    )
```

## Debug Toolbar

Implemente o novo arquivo `cms/ext/debug.py`

```py
from flask_debugtoolbar import DebugToolbarExtension


def configure(app):
    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        DebugToolbarExtension(app)
```

# Configuração das extensões

Algumas extensões requerem configurações adicionais, basta incluir no `cms/settings.yml` para ficar como no abaixo:

> NOTA: fique atento para a identação já que todos os valores estão dentro do escopo de `CMS:`

```yml
CMS:
  SECRET_KEY: 'real_secret_here'
  DB_NAME: cms_db
  SITENAME: Flask CMS
  HOST: '0.0.0.0'
  PORT: 5000
  DEBUG: true
  RELOADER: true

  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure

  DEBUG_TOOLBAR_ENABLED: true
  DEBUG_TB_INTERCEPT_REDIRECTS: false
  DEBUG_TB_PROFILER_ENABLED: true
  DEBUG_TB_TEMPLATE_EDITOR_ENABLED: true

  SIMPLE_LOGIN_HOME_URL: /admin

  FLASK_ADMIN_NAME: Flask CMS!
  FLASK_ADMIN_TEMPLATE_MODE: bootstrap3
  FLASK_ADMIN_SWATCH: default
```

## Crie um usuário para acessar o admin

```bash
cms adduser --username admin --password admin
```

OOOOps  parece que aconteceu um erro?  (sem pânico é proposital) vamos olhar o motivo de não conseguirmos criar o user.. abra o arquivo `cms/cli.py` e veja a função `adduser` perto da linha 40

Implementação atual:

```python
@main.command()
@click.option('--username', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True,
              confirmation_prompt=True)
def adduser(username, password):
    """Cria um novo usuário"""
    try:
        app.db.create_user(username, password)    #  <---  O ERRO ACONTECE AQUI
    except Exception as e:
        click.echo(f'Não foi possivel criar o usuário {username}')
        raise
    else:
        click.echo(f"Usuário {username} criado com sucesso!")
```

O Erro acontece pois estamos tentando acessar `app.db.create_user` fora de um contexto de `app`, precisamos fazer isso sempre dentro de um contexto de app nos casos em que objetos como `request`, `session`, `g` ou `current_app` são necessários, no nosso caso o `database` utiliza o `current_app` portanto no `cms/cli.py` altere a função `adduser` para:

```python
@main.command()
@click.option('--username', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True,
              confirmation_prompt=True)
def adduser(username, password):
    """Cria um novo usuário"""
    try:
        with app.app_context():
            app.db.create_user(username, password)
    except Exception as e:
        click.echo(f'Não foi possivel criar o usuário {username}')
        raise
    else:
        click.echo(f"Usuário {username} criado com sucesso!")
``

Repare que adicionamos `with app.app_context()` é um gerenciador de contexto que forcene aqueles objetos que mencionei ali em cima e entre eles estará o `current_app`

Agora sim salve e execute:

```bash
cms adduser --username admin --password admin

# muitas mensagens de log
Usuário admin criado com sucesso!
```

> NOTA: quanto o `cms/settings.yml` tiver o `DEBUG: false` as mensagens de log não irão mais aparecer.

Execute o app

```bash
cms runserver
``` 

acesse http://localhost:5000/admin e verá a tela de login e então pode fazer o login e acessar o `admin` que por enquanto estará vazio!

![screenshot_2017-10-10_22-55-59](https://user-images.githubusercontent.com/458654/31418738-403d74e0-ae0e-11e7-91f3-71738690ceed.png)

> NOTA: aproveite para dar uma olhada naquela sidebar à direita é a DEBUG Toolbar :)


Vamos adicionar uma extensão de `blog` no admin no próximo passo:


[<<-- anterior](../../../tree/cms_3_config_factory/cms)  -  [próximo -->>](../../../tree/cms_4_blog/cms)
