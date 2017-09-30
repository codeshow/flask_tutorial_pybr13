from flask_debugtoolbar import DebugToolbarExtension


def configure(app):
    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        DebugToolbarExtension(app)
