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
forma dinâmica carregamos as extensões que serão definidas no `settings.yml`

Vamos começar inicializando as extensões básicas e depois customizaremos o 
`admin` e a parte de `autenticação`

No `settings.yml` adicionaremos o item `EXTENSIONS`

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

a primeira coisa a fazer é implementar o `extension factory` em `ext/__init__.py`

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

Agora é só invocar este factory no `app/__init__.py` app factory `create_app`

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
    ext.configure(app)

    return app
```

# Extensões

A primeira extensão que carregamos é a de banco de dados

## TinyMongo

No `ext/database.py`

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

## Autenticação

No `ext/auth.py`

```py
from flask import current_app
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash


def configure(app):
    """Inicializa o Flask Simple Login"""
    SimpleLogin(app, login_checker=login_checker)
    app.db.create_user = create_user

def login_checker(...):

def create_user(...):

```

## Interface admin 

No `ext/admin.py`

```py
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required

# decorate Flask-Admin view via Monkey Patching
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

No `ext/debug.py`

```py
from flask_debugtoolbar import DebugToolbarExtension


def configure(app):
    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        DebugToolbarExtension(app)
```

# Configuração das extensões

Algumas extensões requerem configurações adicionais, basta incluir no `settings.yml`

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
