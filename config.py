from redis import StrictRedis
import logging

class Config(object):
    """自定义配置类,将配置信息以属性的方式罗列即可"""
    DEBUG = True

    # 连接mysql数据库的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    #开启数据库跟踪模式
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #REDIS 数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #具体储存到哪个数据库
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT,db=1)
    #session储存的数据产生后是否session_id是否需要加密
    SESSION_USE_SIGNER = True
    # 是否是永久保存
    SESSION_PERMANENT = False
    # 设置过期时长,默认过期时长31天
    PERMANENT_SESSION_LIFETIME = 86400

class DevelopmentConfig(Config):
    """开发模式"""
    LOG_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    """线上生产环境"""
    LOG_LEVEL = logging.ERROR

#给外界使用提供一个接口
#使用：config_dict["development"] ---->DevelopmentConfig
config_dict = {
    "development" : DevelopmentConfig,
    "production" : ProductionConfig
}

