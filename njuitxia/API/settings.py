from datetime import datetime
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'restful'

PUBLIC_METHODS = ['GET', 'POST']
PUBLIC_ITEM_METHODS = ['GET', 'POST']
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']
ALLOWED_ROLES = ['admin']
# CORS (Cross-Origin Resource Sharing) support.

HATEOAS = False

RETURN_MEDIA_AS_URL = True
MEDIA_ENDPOINT = 'media'

order_schema = {
    'requested_by': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'clients',
            'field': '_id',
            'embeddable': True,
        },
    },
    'status': {
        'type': 'string',
        'allowed': ['waiting', 'working', 'done'],
        'default': 'waiting',
    },
    'handled_by': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'servers',
            'field': '_id',
            'embeddable': True,
        },
    },
    'machine_model': {
        'type': 'string',
        'required': True,
    },
    'OS': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'required': True,
    },
    'comments': {
        'type': 'list',
        'required': False,
        'schema': {
            'type': 'dict',
            'schema': {
                'username': {'type': 'string'},
                'created_at': {'type': 'datetime', 'default': datetime.utcnow()},
                'content': {'type': 'string', 'empty': False},
            },
        },
    },   
}


client_schema = {
    'phone_number': {
        'type': 'string',
        'unique': True,
        'required': True,
        'regex': '^(13|14|15|17|18)[0-9]{9}$',
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
}

server_schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True,
    },
    'password': {
        'type': 'string',
        'required': True,
    },
    'role': {
        'type': 'string',
        'required': True,
        'allowed': ['itxia', 'admin'],
    },
    'email': {
        'type': 'string',
        'regex': '^\S+@\S+$',
        'required': True,
    },
    'campus': {
        'type': 'string',
        'required': True,
        'allowed': ['gulou', 'xianlin'],
    },
}

orders = {
    'schema': order_schema,
    'item_title': 'order',
    'datasource': {
        'default_sort': [('_created', -1)]
    },
}

clients = {
    'schema': client_schema,
    'item_title': 'client',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'phone_number',
    },
    'datasource': {
        'projection': {'phone_number': 1}
    },
}

servers = {
    'schema': server_schema,
    'item_title': 'server',
    'auth_field': 'username',
    'datasource': {
        'projection': {'password': 0}
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },
    'public_methods':[],
}


DOMAIN = {
    'orders': orders,
    'clients': clients,
    'servers': servers,
}
