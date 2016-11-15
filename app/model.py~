from datetime import datetime
from . import db
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask import url_for


class Server(db.Model):
    __tablename__ = 'server'

    id = db.Column('id', db.Integer, primary_key=True)
    password = db.Column('password', db.String(30), nullable=False)
    username = db.Column('username', db.String(30), index=True, unique=True, nullable=False)
    email = db.Column('email', db.String(64), index=True, unique=True, nullable = False)
    campus = db.Column('campus', db.String(10), index=True, nullable=False)
    avatar_picture = db.Column('avatar_picture', db.String(120), default='')
    register_time = db.Column('register_time', db.DateTime, index=True, default=datetime.now)
    

class Form(db.Model):
    __tablename__ = 'form'

    id = db.Column('id', db.Integer, primary_key=True)
    post_time = db.Column('post_time', db.DateTime, default=datetime.now)
    campus = db.Column('campus', db.String(10), index=True, nullable=False)
    status = db.Column('status', db.String(10), index=True, default='waiting', nullable=False)
    machine_model = db.Column('machine_model', db.String(64), nullable=False)
    OS = db.Column('OS', db.String(64), nullable = False)
    description = db.Column('description', db.String(240), nullable=False)
    picture_content = db.Column('picture_content', db.String(900))
    handle_server_id = db.Column('handle_server_id', db.Integer, db.ForeignKey('server.id'))
    handle_server = db.relationship('Server', backref='handle_forms', lazy='dynamic', uselist=True)
    post_client_id = db.Column('post_client_id', db.Integer, db.ForeignKey('client.id'))
    post_client = db.relationship('Client', backref='post_forms', lazy='dynamic', uselist=True)
    
    @hybrid_property
    def pictures(self):
        if not self.picture_content:
            return []
        return self.picture_content.split(', ')


    @pictures.setter
    def pictures(self, urls):
        self.picture_content = ', '.join(urls)
    
    
    def to_json(self):
        json_post = {
            'url': url_for('api1_1.get_form', id=self.id, _external=True),
            'post_client': self.post_client_id,
            'handle_server': self.handle_server_id,
            'campus': self.campus,
            'machine_model': self.machine_model,
            'OS': self.OS,
            'description': self.description,
            'picture_content': self.picture_content,
            'status': self.status,
            'timestamp': self.post_time.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return json_post


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column('id', db.Integer, primary_key=True)
    password = db.Column('password', db.String(30), nullable=False)
    phone_number = db.Column('phone_number', db.String(11), index=True, unique=True, nullable=False)
    email = db.Column('email', db.String(64), index=True, unique=True)
    avatar_picture = db.Column('avatar_picture', db.String(120), default='')
    register_time = db.Column('register_time', db.DateTime, index=True, default=datetime.now)
    
