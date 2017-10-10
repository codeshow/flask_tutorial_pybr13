# 7) WSGI

```bash
cms/                   # module root
├── wsgi.py            # Arquivo para deploy com WSGI servers como gunicorn e uWSGI
```


Fazer deploy com WSGI é bastante simples, a maioria dos servidores de aplicação suporte este padrão.

Na raiz do `cms/` criaremos o arquivo `wsgi.py`

`cms/wsgi.py`


```py
from cms.app import create_app
app = application = create_app(__name__)
```

Repare que existe uma atribuição dupla, pois alguns wsgi servers procuram um objeto chamado `app` e outros adotam `application` então vamos dar a opção a eles.

Agora basta em qualquer local da nossa virtualenv chamar o `gunicorn` com

```bash
# caso não esteja instalado
$ pip install gunicorn

3 executando os workers
$ gunicorn cms.wsgi -w 4 -b "0.0.0.0:8080"
```

Existem outras opções para configurar o Gunicorn mas esta é a linha de comando mais simples

Repare como é importante o `import_name` que passamos para o `create_app`

> OBS:  interessante que no `settings.yml` o DEBUG esteja `false` ao rodar com `wsgi`


[<<-- anterior](../../../tree/cms_6_static/cms)  -  [próximo -->>](../../../tree/cms_8_test/cms)
