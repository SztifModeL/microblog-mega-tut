from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)  # db - obiekt reprezentujacy baze danych
migrate = Migrate(app, db)  # obiekt reprezentujacy silnik migracji

from app import routes, models  # models - modul okresli strukture bazy danych


# Sposob na odpalanie aplikacji
# if __name__ == "__main__":
#     app.run()
    # app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)