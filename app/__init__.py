import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)  # db - obiekt reprezentujacy baze danych
migrate = Migrate(app, db)  # obiekt reprezentujacy silnik migracji

login = LoginManager(app)
login.login_view = 'login'

if not app.debug:  # jesli nie jest w trybie debug
    if app.config['MAIL_SERVER']:  # i jesli skonfigurowany jest server poczty -> wysylanie bledow na maila
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)  # ustawia poziom raportowania tylko na bledy
        app.logger.addHandler(mail_handler)  # dolacza SMTPHandler do obiektu Flask

    if not os.path.exists('logs'):  # i jesli katalog logow nie istnieje -> tworzy go i zapisuje bledoy do pliku
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)  # ogranicza plik do 10KB i zapis do ostatnich 10 backupow
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors  # models - modul okresli strukture bazy danych


# Sposob na odpalanie aplikacji
if __name__ == "__main__":
    app.run(debug=False)