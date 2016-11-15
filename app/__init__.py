# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from config import config
import redis
from qiniu import Auth, put_file, etag, urlsafe_base64_encode


app = Flask(__name__)

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    app.redis = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
                            db=app.config['REDIS_DB'])

    app.q = Auth(access_key=app.config['QINIU_ACCESS_KEY'], secret_key=app.config['QINIU_SECRET_KEY'])
    app.bucket_name = app.config['BUCKET_NAME']
    
    app.debug = app.config['DEBUG']
    
    
    db.init_app(app)
    from .api_1_1 import api as api_1_1_blueprint
    app.register_blueprint(api_1_1_blueprint, url_prefix='/api/v1_1')
    
    return app
