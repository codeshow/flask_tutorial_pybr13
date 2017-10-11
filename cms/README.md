# 4) Criando um módulo de Blog

```bash
cms/                   # module root
├── ext/               # Extensões (Blueprints) do app
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Agora é hora de criar nosso primeiro Blueprint que irá adicionar a funcionalidade
de `Blog` ao CMS.

Para começar vamos adicionar o factory do blog no `cms/settings.yml`


```yml
  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure
    - cms.ext.blog.configure         # <-- Nova extensão
```

Agora vamos implementar o novo arquivo `cms/ext/blog.py`


```py
from slugify import slugify
from flask import Blueprint, render_template, abort, current_app
from wtforms import form, fields, validators
from .admin import ModelView

blog_blueprint = Blueprint('blog', __name__, template_folder='template')


# Front end

@blog_blueprint.route('/')
def index():
    """Exibe todos os posts"""
    posts = current_app.db.blog.find({'publicado': True})
    return render_template('blog.html', posts=posts)


@blog_blueprint.route('/<slug>.html')
def view_post(slug):
    """Exibe /slug-do-post.html"""
    post = current_app.db.blog.find_one({'publicado': True, 'slug': slug})
    if not post:
        abort(404, 'Post não encontrado')
    return render_template('post.html', post=post)


# Admin

class BlogForm(form.Form):
    """Formulário para criação da postagem no blog"""
    titulo = fields.StringField('Titulo', [validators.required()])
    slug = fields.HiddenField('Slug')
    texto = fields.TextAreaField('Texto')
    autor = fields.StringField('Autor')
    publicado = fields.BooleanField('Publicado', default=True)


class AdminBlog(ModelView):
    column_list = ('titulo', 'slug', 'autor', 'publicado')
    form = BlogForm

    def on_model_change(self, form, post, is_created):
        """Permite alterar e validar dados do formulário"""
        post['slug'] = slugify(post['titulo']).lower()
        if is_created and current_app.db.blog.find_one({'slug': post['slug']}):
            raise validators.ValidationError('Titulo duplicado')


# Factory

def configure(app):
    """Carrega a extensão Blog"""
    # adiciona o item no /admin
    app.admin.add_view(AdminBlog(app.db.blog, 'Blog'))

    # registra o BP com / e /slug-do-post.html
    app.register_blueprint(blog_blueprint)

```

E como pode perceber se tentar rodar no console `cms runserver` e acessar http://localhost:5000 verá um erro
informando que o Jinja não encontrou o template `blog.html`

![screenshot_2017-10-10_23-05-20](https://user-images.githubusercontent.com/458654/31418983-81474406-ae0f-11e7-9c16-60b0d1967507.png)


Vamos criar o `cms/templates/blog.html`


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{config.SITENAME}}</title>
</head>
<body>
    <h1>{{config.SITENAME}} - Todas as postagens </h1>
    <ul>
    {% for post in posts %}
       <li>    
            <a href="{{url_for('blog.view_post', slug=post.slug)}}">
                {{post.titulo}}
            </a><br>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

e o `cms/templates/post.html`


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{post.titulo}}</title>
</head>
<body>
    <h1>{{post.titulo}}</h1>
    <small>por {{post.autor}}</small>
    <p>
        {{post.texto}}
    </p>
    <a href="{{url_for('blog.index')}}">Voltar</a>
</body>
</html>
```

rode `cms runserver`

Agora vá em http://localhost:5000/admin e adicione alguns posts! 

![screenshot_2017-10-10_23-07-38](https://user-images.githubusercontent.com/458654/31419029-d37d0daa-ae0f-11e7-80fd-8679b803ecdd.png)


clique no `salvar` e verá

![screenshot_2017-10-10_23-08-15](https://user-images.githubusercontent.com/458654/31419044-ea26b5ec-ae0f-11e7-952d-81db73b26801.png)


então acesse em http://localhost:5000 para ver as postagens

![screenshot_2017-10-10_23-09-05](https://user-images.githubusercontent.com/458654/31419082-10842a3a-ae10-11e7-8ad5-5016d3565f65.png)

e acesse http://localhost:5000/nova-postagem-no-blog.html para ler a noticia

![screenshot_2017-10-10_23-09-20](https://user-images.githubusercontent.com/458654/31419092-210c9dd8-ae10-11e7-8134-82e7b75392fc.png)


**NOOOSAAA como está feio esse layout!!!!***

OK..

Próximo passo é melhorar nossos templates com Jinja e Bootstrap!


[<<-- anterior](../../../tree/cms_3_extension_factory/cms)  -  [próximo -->>](../../../tree/cms_5_jinja/cms)

