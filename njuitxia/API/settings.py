# -*- coding: utf-8 -*-

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'

SOFT_DELETE = True
HATEOAS = False

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# 订单：
#    - phone_number:
#       手机号码
#    - name:
#       姓名
#    - lilybbs_id:
#       小百合 ID
#    - campus:
#       校区
#    - machine_model:
#       机器型号
#    - description:
#       问题描述
#    - status:
#       订单状态
#    - comments:
#       订单回复
order_schema = {
    'phone_number': {
        'type': 'string',
        'regex': '^(13|14|15|17|18)[0-9]{9}$',
        'required': True,
    },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
    },
    'lilybbs_id': {
        'type': 'string',
    },
    'campus': {
        'type': 'string',
        'required': True,
        'allowed': ['gulou', 'xianlin'],
    },
    'machine_model': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'required': True,
    },
    'status': {
        'type': 'integer',
        'allowed': [0, 1, -1], # 0: 等待处理，1: 正在处理，-1: 处理完成。
        'default': 0,
    },
    'comments': {
        'type': 'list',
        'required': False,
        'schema': {
            'type': 'dict',
            'schema': {
                'username': {'type': 'string'},
                'created_at': {'type': 'datetime'},
                'content': {'type': 'string', 'empty': False},
            },
        },
    },
}

orders = {
    'schema': order_schema,
}

DOMAIN = {
    'orders': orders,
}
