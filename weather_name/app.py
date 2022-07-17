# -*- coding: utf-8 -*-
import os

from flask import Flask

from weather_name import views
from weather_name.extensions import db, migrate


CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")


def create_app(config_object="weather_name.settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(views.blueprint)
    return app
