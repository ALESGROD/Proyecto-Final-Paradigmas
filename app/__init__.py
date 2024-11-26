from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Ruta de la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar advertencias

    db.init_app(app)  # Inicializar la base de datos
    migrate.init_app(app, db)  # Inicializar Flask-Migrate

    from .routes import main
    app.register_blueprint(main)

    return app
