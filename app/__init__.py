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

from app import routes, models, errors  # models - modul okresli strukture bazy danych


# Sposob na odpalanie aplikacji
if __name__ == "__main__":
    app.run(debug=False)