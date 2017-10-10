# 3) Application factory

```bash             # Testes com py.test
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── cli.py             # Ferramenta de linha de comando `cms --help`
```

Factory é um padrão recomendado pela [documentação oficial do Flask](http://flask.pocoo.org/docs/0.12/patterns/appfactories/#basic-factories) a idéia é bastante simples e ela ajuda a evitar problemas de [circular imports](http://pythonclub.com.br/what-the-flask-pt-2-flask-patterns-boas-praticas-na-estrutura-de-aplicacoes-flask.html#circular_imports) e também melhora a composição do projeto através de extensões.

**factory** nada mais é do que uma **função** ou **Classe** que recebe como primeiro parametro o **app** e então **altera** ou **adiciona** alguma funcionalidade ou configuração durante a **fase de configuração** do nosso projeto.

Exemplo:

```python
def create_object():
    """factory inicial cria o novo objeto"""
    obj = {}  # neste exemplo é um dicionário vazio
    return obj

def factory_add_foo(x):
    x['foo'] = 'bar'
    
def factory_enable_debug(x):
    x['DEBUG'] = True

obj = create_object()
factory_add_foo(obj)
factory_enable_debug(obj)
...
```

No final temos um objeto composto pelas funcionalidades das **factories**

```python
print(obj)
{'foo': 'bar', 'DEBUG': True}
```

Então agora imagine que o **obj** do exemplo acima é uma **app** `Flask` e aplicamos o mesmo conceito compondo a **app** através de extensões que são **functions** ou **Classes** que recebem o **app** como primeiro argumento. 

## implementação de `app/__init__.py` com o application factory.

```py
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Faça o que quiser com o `app` aqui:

    return app

```

e então no `cli.py` importamos esse factory

```py
from cms.app import create_app

app = create_app()
```

A partir daqui já podemos executar alguns comandos:

```bash

$ cms shell
>>> app.config

# ou

$ cms runserver --port 8000
* Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
```

No entanto se rodarmos o `cms adduser` teremos mais um erro:

```bash
$ cms adduser
Username: 
Password:
Repeat password:
...

AttributeError: 'Flask' object has no attribute 'db'

```

Ainda precisamos terminar de configurar o `app` e adicionar a conexão com um banco de
dados. (falarei mais dos detalhes a respeito em breve)

Mas antes vamos agora criar o `config factory`


[<<-- anterior](../../../tree/cms_2_cli/cms)  -  [próximo -->>](../../../tree/cms_3_config_factory/cms)

