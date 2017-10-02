from mistune import markdown


def configure(app):
    # adiciona {{ markdown('texto) }} para os templates
    app.add_template_global(markdown)
