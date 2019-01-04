from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict
from flask import Flask

import logging
from logging.handlers import RotatingFileHandler


#创建mysql数据库对象
db = SQLAlchemy()

redis_store = None #type:StrictRedis

def write_log(config_class):
    """记录日至方法"""

    # 设置日志的记录等级
    logging.basicConfig(level=config_class.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=10, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
    """
    将与app相关的配置方法写dao工厂方法
    :return app对象
    """



    app = Flask(__name__)


    #根据development建获取对应的配置类名
    config_class = config_dict[config_name]
    app.config.from_object(config_class)
    # 0写入日志
    write_log(config_class)
    #创建数据库对象
    db.init_app(app)


    #3创建redis数据库对象(懒加载思想)
    global redis_store
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port = config_class.REDIS_PORT)

    #4开启CSRF保护机制
    CSRFProtect(app)
    #5借助session调整flask.session的储存位置到redis中
    Session(app)

    #注册蓝图
    #将蓝图的导入延迟到工厂方法中,能够解决导入循环问题

    from info.modules.index import index_bp
    app.register_blueprint(index_bp)


    return app