import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')  # Flask-SQLAlchemy pobiera lokalizacje bazy danych aplikacji ze SQLALCHEMY_DATABASE_URIzmiennej konfiguracyjnej, biore adres URL bazy danych ze DATABASE_URL zmiennej srodowiskowej, a jesli to nie jest zdefiniowane, konfiguruje baze danych o nazwie app.db znajdujaca sie w glownym katalogu aplikacji, ktora jest przechowywana w basedir zmiennej
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['modeltest@wp.pl']