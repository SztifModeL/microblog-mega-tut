import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')  # Flask-SQLAlchemy pobiera lokalizacje bazy danych aplikacji ze SQLALCHEMY_DATABASE_URIzmiennej konfiguracyjnej, biore adres URL bazy danych ze DATABASE_URL zmiennej srodowiskowej, a jesli to nie jest zdefiniowane, konfiguruje baze danych o nazwie app.db znajdujaca sie w glownym katalogu aplikacji, ktora jest przechowywana w basedir zmiennej
    SQLALCHEMY_TRACK_MODIFICATIONS = False