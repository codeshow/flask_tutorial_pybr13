from pathlib import Path
from tinymongo import TinyMongoClient


def configure(app):
    """Inicia o client do TinyMongo e adiciona `app.db`
    *para usar MongoDB basta mudar para `pymongo.MongoClient`
    """
    db_folder = app.config.get('DB_FOLDER', 'database')
    db_name = app.config.get('DB_NAME', 'cms_db')

    foldername = Path(db_folder) / Path(app.root_path) / Path('database')
    client = TinyMongoClient(foldername=foldername)

    app.db = client[db_name]
