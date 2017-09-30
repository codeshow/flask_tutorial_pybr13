# 3) Application factory

```bash             # Testes com py.test
cms/                   # module root
├── app/               # Application Factory (Flask app será iniciada aqui)
├── cli.py             # Ferramenta de linha de comando `cms --help`
```


agora nós temos a implementação de `app/__init__.py` com o application factory.

```py
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Faça o que quiser com o `app` aqui:

    return app

```

e então no `cli.py` importamos esse factory

```py
from .app import create_app

app = create_app()
```

A partir daqui já podemos executar alguns comandos:

```bash

$ cms shell
>>> app.


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
