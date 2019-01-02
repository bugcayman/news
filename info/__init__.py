from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict
from flask import Flask

#创建mysql数据库对象
db = SQLAlchemy()

redis_store = None #type:StrictRedis
def create_app(config_name):
    """
    将与app相关的配置方法写dao工厂方法
    :returnapp对象

    """
    app = Flask(__name__)


    #根据development建获取对应的配置类名
    config_class = config_dict[config_name]
    app.config.from_object(config_class)
    #创建数据库对象
    db.init_app(app)


    #3创建redis数据库对象(懒加载思想)
    global redis_store
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port = config_class.REDIS_PORT)

    #4开启CSRF保护机制
    CSRFProtect(app)
    #5借助session调整flask.session的储存位置到redis中
    Session(app)
