# -*- coding: utf-8 -*-
from flask import Flask
from config import basedir
from config import config
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
Base = db.Model
PAGE = None
#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'fq_h5_m.login'

limiter = None

def init_mongo_db(config_name='default'):
    from mongokit import Connection
    return Connection(
        config[config_name].MONGODB_HOST,
        config[config_name].MONGODB_PORT
    )

def init_scripts_db(config_name):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine(config[config_name].SQLALCHEMY_DATABASE_URI, echo=False)
    return sessionmaker(bind=engine)()
    #global Base
    #Base = declarative_base()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    global limiter
    limiter = Limiter(
        app,
        key_func=get_remote_address
    )


    global PAGE
    PAGE = config[config_name].PAGE

    # login_manager.init_app(app)
    db.init_app(app)

    from .app import apply as app_blueprint
    app.register_blueprint(app_blueprint, url_prefix='/api/v1')

    return app

