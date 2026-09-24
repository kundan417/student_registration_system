from flask import Flask
from app.models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "12345678"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    db.init_app(app)

    migrate = Migrate(app,db)

    from app.routes import main
    app.register_blueprint(main)

    return app