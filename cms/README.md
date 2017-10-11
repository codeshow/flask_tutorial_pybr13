# 8) Testes

```bash
tests/
```

Hora de testar a aplicação usando o Py.Test

primeiro configuramos o `py.test` no `tests/conftest.py`


```py
import pytest
from cms.app import create_app


@pytest.fixture
def app():
    """Flask Pytest uses it"""
    return create_app('cms')
```

Agora todos nossos testes terão em seu escopo a fixture `app` e então usaremos `app.app_context()` e o `app.test_client()` dependendo do tipo de teste.

- app.app_context
  fornece um contexto `mock` da app, prove os objetos `request`, `session` , `g` , `current_app` para acessarmos durante os testes

- app.test_client
  fornece uma espécie de **headless browser** que responde a métodos HTTP get, post, put, delete etc...


```py


def test_config_sitename(app):
    assert app.config.SITENAME == 'Flask CMS'


def test_can_create_find_delete_blog_post(app):
    with app.app_context():
        # create
        app.db.blog.insert_one(
            {
                'titulo': 'Este é um teste',
                'slug': 'este-e-um-teste',
                'autor': 'Mikael Scott',
                'texto': 'Texto **teste**',
                'publicado': True
            }
        )
        # find
        assert app.db.blog.find({'slug': 'este-e-um-teste'}).count() == 1
        # delete
        app.db.blog.delete_one({'slug': 'este-e-um-teste'})


def test_can_request_a_post(app):
    # create a blog post
    app.db.blog.insert_one(
        {
            'titulo': 'Este é um teste',
            'slug': 'este-e-um-outro-teste',
            'autor': 'Mikael Scott',
            'texto': 'Texto **teste**',
            'publicado': True
        }
    )
    with app.test_client() as client:
        response = client.get('/este-e-um-outro-teste.html')
        assert response.status_code == 200
        assert '<strong>teste</strong>' in str(response.data)
        assert 'Por <a href="#">Mikael Scott</a>' in str(response.data)
        # beautiful soup / selenium?

    # clean up
    app.db.blog.delete_one({'slug': 'este-e-um-outro-teste'})
```


[<<-- anterior](../../../tree/cms_7_wsgi/cms)  -  [próximo -->>](../../../tree/cms_9_deploy/cms)
