

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
