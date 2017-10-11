# 5) Adicionando template globals

```bash
cms/                   # module root
├── ext/               # Extensões (Blueprints) do app
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Acesse o http://localhost:5000/admin/blogview/new/ e crie um novo blog post usando o formato markdown.

```
titulo:  
Novo post

texto:
# Este e meu novo post
- item da lista
- outro item
> isso é uma citação

![image](http://lorempixel.com/400/400)

Autor:
Seu Nome

publicado: 
True (marque o checkbox)
```

Salve este post e acesse http://localhost:5000 e clique no post.

Você irá perceber que o texto que aparece é o markdown puro sem renderizar, precisamos fazer o render do markdown para transformar em HTML.

![screenshot_2017-10-10_23-19-53](https://user-images.githubusercontent.com/458654/31419311-89d9e1ee-ae11-11e7-9363-3d9a75f0f830.png)



Para isso vamos usar a lib `mistune` e inicializar em uma nova extensão portanto crie o arquivo `cms/ext/markdown.py`

```py
from mistune import markdown

def configure(app):
    # adiciona {{ markdown('texto) }} para os templates
    app.add_template_global(markdown)
```

> A extensão acima adiciona ao contexto do `Jinja` a função global `markdown` que irá receber um texto e transformar em HTML

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


A partir de agora podemos editar o template `cms/templates/post.html` e fazer a renderização do markdown para html conforme o template abaixo:

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
    <p>{{ markdown(post.texto)}}</p>  <!-- AQUI ESTAMOS CHAMANDO A FUNCAO MARKDOWN -->
</div><!-- /.blog-post -->
{% endblock %}
```


No console `CTRL+C` para parar e rode novamente `cms runserver` e acesse http://localhost:5000

Repare que agora temos o HTML puro ao acessar o post, ainda não é o que queremos

![screenshot_2017-10-10_23-22-59](https://user-images.githubusercontent.com/458654/31419382-f7d8bdaa-ae11-11e7-93e0-3e64dd371af2.png)

temos 2 opções para resolver isso.

`Markup`

O Jinja irá fazer o `escape` de tags html por questões de segurança, quando queremos dizer a ele que o texto em questão é seguro e pode ser renderizado temos que marcar como seguro, e a primeira forma é usar o `Markup` que é uma classe que recebe um texto e adiciona um método especial `__html__` (similar ao `__str__`) ao texto que foi passado.

podemos alterar o `cms/ext/markdown.py` para:

```py
import mistune
from flask import Markup

def markdown(texto):
    return Markup(mistune.markdown(texto))


def configure(app):
    # adiciona {{ markdown('texto) }} para os templates
    app.add_template_global(markdown)
```

Ou podemos de uma forma mais simples fazer isso direto no template `cms/templates/post.html` usando o filtro `| safe`

> NOTA:  ao usar o método abaixo, o uso de `Markup` não é necessário.

```html
 <p>{{ markdown(post.texto) | safe }}</p>
```


[<<-- anterior](../../../tree/cms_5_jinja/cms)  -  [próximo -->>](../../../tree/cms_6_static/cms)


