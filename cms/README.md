# 4) Criando um módulo de Blog

```bash
cms/                   # module root
├── ext/               # Extensões (Blueprints) do app
├── templates/         # Templates Jinja2
└── settings.yml       # Configurações que serão carregadas
```

Agora é hora de criar nosso primeiro Blueprint que irá adicionar a funcionalidade
de `Blog` ao CMS.

Para começar vamos adicionar o factory do blog no `settings.yml`


```yml
  EXTENSIONS:
    - cms.ext.database.configure
    - cms.ext.admin.configure
    - cms.ext.auth.configure
    - cms.ext.debug.configure
    - cms.ext.blog.configure         # <-- Nova extensão
```

Agora vamos implementar em `ext/blog.py`


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

E como pode perceber se tentar rodar `cms runserver` e acessar http://localhost:5000 verá um erro
informando que o Jinja não encontrou o template `blog.html`

Vamos criar o `templates/blog.html`


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

e o `templates/post.html`


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

Agora vá em http://localhost:5000/admin e adicione alguns posts! e acesse em http://localhost:5000


Próximo passo é melhorar nossos templates com Jinja!


[<<-- anterior](../../../tree/cms_3_extension_factory/cms)  -  [próximo -->>](../../../tree/cms_5_jinja/cms)

