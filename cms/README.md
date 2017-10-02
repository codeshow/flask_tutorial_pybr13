# 6) Acessando arquivos estáticos

```bash
cms/                   # module root
├── static/            # Arquivos estáticos (.css, .js, .images)
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Vamos agora colocar um arquivo estático em nossa pasta `static` e ver como é fácil acessar através dos templates.

Vamos utilizar o https://bootswatch.com/ que contém uma série de temas para Bootstrap, salvaremos 2 deles na pasta static.

https://bootswatch.com/cerulean/bootstrap.min.css - > `static/swatch-cerulean.css`

https://bootswatch.com/united/bootstrap.min.css - > `static/swatch-united.css`


Digamos que agora queiramos carregar o tema cerulean em nosso template `base.html` basta editar incluindo o bloco `styles` suportado pelo `Flask-Bootstrap` e não se esquecer de chamar o `super()`


```html
{% block styles %}
{{super()}}
<link rel="stylesheet" href="{{url_for('static', filename='css/swatch-cerulean.css')}}">
{% endblock %}
```

bem simples! agora basta acessar e ver o novo visual aplicado ao blog.

Vamos agora deixar isso dinamico.

No `settings.yml`

```yaml
CMS:
  ...
  SWATCH: united
  ...
```

e agora basta ler a config direto no template


```html
{% block styles %}
{{super()}}
<link rel="stylesheet"
      href="{{url_for('static', filename='css/swatch-{0}.css'.format(config.SWATCH))}}">
{% endblock %}
``` 


O acesso a qualquer outro tipo de arquivo estático é feito da mesma maneira `url_for('static', filename='')` caso o seu blueprint tenha uma pasta especifica para arquivos estaticos basta usar `.` ou o nome do Blueprint ex: `url_for('blog.static', filename='')` ou `url_for('.static', filename='')` (dentro de um template renderizado pelo blueprint)
