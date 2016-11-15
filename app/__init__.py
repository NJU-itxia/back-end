# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from sqlalchemy.ext.declarative import declarative_base
from config import config
from qiniu import Auth, put_file, etag, urlsafe_base64_encode


app = Flask(__name__)

db = SQLAlchemy()
redis = FlaskRedis()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.q = Auth(access_key=app.config['QINIU_ACCESS_KEY'], secret_key=app.config['QINIU_SECRET_KEY'])
    app.bucket_name = app.config['BUCKET_NAME']
    
    app.debug = app.config['DEBUG']
    
    
    db.init_app(app)
    redis.init_app(app)
    
    from .api_1_1 import api as api_1_1_blueprint
    app.register_blueprint(api_1_1_blueprint, url_prefix='/api/v1_1')
    
    return app
