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
