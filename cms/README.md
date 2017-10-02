# 5) Jinja templates

```bash
cms/                   # module root
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Agora vamos entender alguns componentes do `Jinja2` como:

- Herança de template base
- blocos
- includes
- Filtros


Para facilitar a nossa vida vamos usar a extensão `Flask-Bootstrap` instalada com `pip install flask_bootstrap` esta extensão fornece os templates base para que tenhamos os layouts do `bootstrap` facilmente na app.

Comece incluindo o `FlaskBootstrap` como nova extensao no `settings.yml`


```yaml
  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure
    - cms.ext.blog.configure
    - flask_bootstrap.Bootstrap   # <-- Nova extensão
```

> O nosso `extension factory` aceita qualquer `callable` que receba `app` como argumento, portanto podemos carregar extensões externas aqui.


Agora vamos ajustar os teplates para usar o FlaskBootstrap

`templates/base.html`

```html
{% extends "bootstrap/base.html" %}

{% block title %} {{config.SITENAME}} {% endblock %}

{% block navbar %}{% include 'navbar.html'%}{% endblock %}

{% block content %}
<div class="container">
    {% block blogheader %}
        <div class="blog-header">
        <h1 class="blog-title">
            {{config.TITLE | default('Add title to config.TITLE', True)}}
        </h1>
        <p class="lead blog-description">
            {{config.DESCRIPTION | default('Add description to config.DESCRIPTION', True)}}
        </p>
        </div>
    {% endblock %}
    <div class="row">
        <div class="col-sm-8 blog-main">
            {% block main %}{% endblock %}
            {% include 'pager.html'%}
        </div><!-- /.blog-main -->
        {% include 'sidebar.html' %}
    </div><!-- /.row -->
</div><!-- /.container -->
{% endblock %}

```

`templates/blog.html`

```html
{% extends "base.html" %}

{% block main %}

    {% for post in posts %}
        <div class="blog-post">
            <h2 class="blog-post-title">
                <a href="{{url_for('blog.view_post', slug=post.slug)}}">
                    {{post.titulo}}
                </a>
            </h2>
            <p class="blog-post-meta">Por {{post.autor}}</a></p>
            <p>{{post.texto[:140]}}</p>
        </div><!-- /.blog-post -->
    {% endfor %}

{% endblock %}
```



`templates/post.html`

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
    <p>{{ post.texto }}</p>
</div><!-- /.blog-post -->
{% endblock %}
```


`templates/sidebar.html`

```html
<div class="col-sm-3 col-sm-offset-1 blog-sidebar">
    {% block sidebar %}
    <div class="sidebar-module sidebar-module-inset">
    <h4>About</h4>
    <p>{{config.ABOUT|default('Add text to config.ABOUT', True)}}</p>
    </div>
    <div class="sidebar-module">
    <h4>Links</h4>
    <ol class="list-unstyled">
        {% for name, url in config.get('LINKS', []) %}
          <li><a href="{{url}}">{{name}}</a></li>
        {% else %}
          Add links to config.LINKS 
        {% endfor %}
    </ol>
    </div>
{% endblock %}
</div><!-- /.blog-sidebar -->
```


`templates/navbar.html`

```html
<nav class="navbar navbar-default">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">{{config.SITENAME}}</a>
        </div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="{{url_for('blog.index')}}">Home</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
            {% if session.simple_logged_in %}
                <li><a>Logged in as {{session.simple_username}}</a></li>
                <li><a href="{{url_for('simplelogin.logout')}}">logout</a></li>
            {% else %}
                <li><a href="{{url_for('simplelogin.login')}}">login</a></li>  
            {% endif %}
        </ul>
    </div><!--/.container -->
</nav>
```


`templates/pager.html`

```html
<hr>
<nav>
    <ul class="pager">
    <li><a href="#">Previous</a></li>
    <li><a href="#">Next</a></li>
    </ul>
</nav>
```

Agora executando o `cms runserver` o nosso layout já estará completamente renovado!


> Porém você verá algumas mensagens de placeholder como `adicione config.DESCRIPTION`

Então vamos completar o `settings.yml`

```yaml
CMS:
  ...
  TITLE: Hello
  DESCRIPTION: Awesome Blog
  ABOUT: This is my blog, I am xyz
  LINKS:
    - ['Github', 'http://github.com']
    - ['Twitter', 'http://twitter.com']
  
  ...

```
