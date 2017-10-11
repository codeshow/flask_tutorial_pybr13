# 6) Acessando arquivos estáticos

```bash
cms/                   # module root
├── static/            # Arquivos estáticos (.css, .js, .images)
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Vamos agora colocar um arquivo estático em nossa pasta `static` e ver como é fácil acessar através dos templates.

primeiro crie a pasta `cms/static/css`

```bash
mkdir -p cms/static/css
```


Vamos utilizar o https://bootswatch.com/ que contém uma série de temas para Bootstrap, salvaremos 2 deles na pasta static.

Clique bom o botão direito e `salvar link como..` para as pastas indicadas e com os nomes indicados

https://bootswatch.com/cerulean/bootstrap.min.css - > `static/css/swatch-cerulean.css`

https://bootswatch.com/united/bootstrap.min.css - > `static/css/swatch-united.css`

Se preferir faça via linha de comando se tiver o `wget` disponivel, estando na pasta raiz do projeto (onde vc clonou o repositorio)

```bash
wget https://bootswatch.com/cerulean/bootstrap.min.css -O cms/static/css/swatch-cerulean.css
wget https://bootswatch.com/united/bootstrap.min.css -O cms/static/css/swatch-united.css
```
> DICA: pode repetir o processo acima para os outros temas disponiveis no bootswatch


Digamos que agora queiramos carregar o tema cerulean em nosso template `cms/templates/base.html` basta editar incluindo o bloco `styles` suportado pelo `Flask-Bootstrap` e não se esquecer de chamar o `super()`

coloque no final do arquivo `cms/templates/blog.html`

```html
{% block styles %}
{{super()}}
<link rel="stylesheet" href="{{url_for('static', filename='css/swatch-cerulean.css')}}">
{% endblock %}
```

a função global `url_for` cria url para acessar os arquivos estáticos basta passar `static` como primeiro argumento e `filename` contendo o caminho do arquivo que deseja acessar.

bem simples! agora basta reiniciar `cms runserver` e acessar http://localhost:5000 e ver o novo visual aplicado ao blog.


![screenshot_2017-10-10_23-39-19](https://user-images.githubusercontent.com/458654/31419809-41a34ade-ae14-11e7-9285-6595a3ea4bf0.png)


Alterando para:

```html
{% block styles %}
{{super()}}
<link rel="stylesheet" href="{{url_for('static', filename='css/swatch-united.css')}}">
{% endblock %}
```

![screenshot_2017-10-10_23-40-29](https://user-images.githubusercontent.com/458654/31419841-6b72d32a-ae14-11e7-8957-cb5f13325fbc.png)



Vamos agora deixar isso dinâmico.

No `cms/settings.yml`

```yaml
CMS:
  ...
  SWATCH: cerulean
  ...
```

e agora basta ler a config direto no template `cms/templates/base.html`


```html
{% block styles %}
{{super()}}
<link rel="stylesheet"
      href="{{url_for('static', filename='css/swatch-{0}.css'.format(config.SWATCH))}}">
{% endblock %}
``` 

![screenshot_2017-10-10_23-42-48](https://user-images.githubusercontent.com/458654/31419888-bd8a325c-ae14-11e7-8ea1-5a94b484a788.png)

> NOTA: lembre-se de reiniciar com ctrl+C e depois `cms runserver` para ver as midanças pois o reloader não monitora arquivos estáticos.

O acesso a qualquer outro tipo de arquivo estático é feito da mesma maneira `url_for('static', filename='')` caso o seu blueprint tenha uma pasta especifica para arquivos estaticos basta usar `.` ou o nome do Blueprint ex: `url_for('blog.static', filename='')` ou `url_for('.static', filename='')` (dentro de um template renderizado pelo blueprint)

Experimente com os outros temas do bootswatch!


[<<-- anterior](../../../tree/cms_5_template_globals/cms)  -  [próximo -->>](../../../tree/cms_7_wsgi/cms)

