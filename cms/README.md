# 5) Adicionando template globals

```bash
cms/                   # module root
├── ext/               # Extensões (Blueprints) do app
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Acesse o admin e crie um novo blog post usando o formato markdown.

```
titulo:  Novo post
texto:
    # Este e meu novo post
    - item da lista
    - outro item
    > isso é uma citação
    ![image](http://lorempixel.com/400/400)
publicado: True
```

Salve este post e acesse http://localhost:5000 e clique no post.

Você irá perceber que o texto que aparece é o markdown puro sem renderizar, precisamos fazer o render do markdown para transformar em HTML.

Para isso vamos usar a lib `mistune` e inicializar em uma nova extensão em `cms/ext/markdown.py`

```py
from mistune import markdown

def configure(app):
    # adiciona {{ markdown('texto) }} para os templates
    app.add_template_global(markdown)
```

> A extensão acima adiciona ao cotnexto fo `Jinja` a global `markdown`

Agora será preciso carregar a nova extensão no `settings.yml`


```yml
  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure
    - cms.ext.blog.configure
    - flask_bootstrap.Bootstrap
    - cms.ext.markdown.configure  # < ---- Nova extensão
```


A partir de agora podemos editar o template `post.html` e fazer a renderização do markdown para html

```html

{% extends "base.html" %}

{% block title %} {{post.titulo}} - {{super()}} {% endblock %}

{% block blogheader %}
<div class="blog-header">
  <h1 class="blog-title">{{post.titulo}}</h1>
</div>
{% endblock %}

{% block main %}
<div class="blog-post">
    <p class="blog-post-meta">Por <a href="#">{{post.autor}}</a></p>
    <p>{{ markdown(post.texto)}}</p>
</div><!-- /.blog-post -->
{% endblock %}
```


Repare que agora temos o HTML puro ao acessar o post, ainda não é o que queremos, temos 2 opções para resolver isso.


`Markup`

```py
import mistune
from flask import Markup

def markdown(texto):
    return Markup(mistune.markdown(texto))


def configure(app):
    # adiciona {{ markdown('texto) }} para os templates
    app.add_template_global(markdown)
```

Ou podemos de uma forma mais simples fazer isso no template usando o filtro `safe`


```html
 <p>{{ markdown(post.texto) | safe }}</p>
```


[<<-- anterior](../../../tree/cms_5_jinja/cms)  -  [próximo -->>](../../../tree/cms_6_static/cms)


