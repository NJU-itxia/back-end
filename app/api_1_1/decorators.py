# coding:utf-8
from flask import request, jsonify, current_app
from functools import wraps


def login_check(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'code': 0, 'message': '需要验证'})

        phone_number = current_app.redis.get('token:%s' % token)
        if not phone_number or token != current_app.redis.hget('client:%s' % phone_number, 'token'):
            return jsonify({'code': 2, 'message': '验证信息错误'})

        return f(*args, **kwargs)
    return decorator
