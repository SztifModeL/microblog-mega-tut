import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \  # Flask-SQLAlchemy pobiera lokalizację bazy danych aplikacji ze SQLALCHEMY_DATABASE_URIzmiennej konfiguracyjnej
        'sqlite:///' + os.path.join(basedir, 'app.db')  # biorę adres URL bazy danych ze DATABASE_URLzmiennej środowiskowej, a jeśli to nie jest zdefiniowane, konfiguruję bazę danych o nazwie app.db znajdującą się w głównym katalogu aplikacji, która jest przechowywana w basedirzmiennej
    SQLALCHEMY_TRACK_MODIFICATIONS = False