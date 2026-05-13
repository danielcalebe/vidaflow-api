from flask import Flask

from app.config import Config
from app.extensions import db, migrate, jwt

from app.routes.auth_routes import auth_bp
from app.routes.habit_routes import habit_bp
from app.routes.tip_routes import tip_bp
from app.routes.status_routes import status_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(habit_bp)
    app.register_blueprint(tip_bp)
    app.register_blueprint(status_bp)

    return app