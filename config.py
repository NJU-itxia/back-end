class Config(object):
    SECRET_KEY = 'saduhsuaihfe332r32rfo43rtn3noiYUG9jijoNF23'
    QINIU_ACCESS_KEY = '2SDKEG3KlbfHAHhT_Ajj5UyZY_mgNo1HZS-2yiJM'
    QINIU_SECRET_KEY = 'sewuf9u7Gq_s8GvBpZld0x_y5VDZwzHp4awJxSS9'
    BUCKET_NAME = 'itxia'
    FLASKY_POSTS_PER_PAGE = 20


class DevelopmentConfig(Config):
    DEBUG = True

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_PASSWORD = ''

    SQLALCHEMY_DATABASE_URI = "mysql://root:cliff522..@localhost/api?charset=utf8"


class ProductionConfig(Config):
    DEBUG = False

    REDIS_HOST = 'server-ip'
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_PASSWORD = ''

    SQLALCHEMY_DATABASE_URI = "mysql://root:cliff522..@localhost/api?charset=utf8"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
