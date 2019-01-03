from info.modules.index import index_bp
#2.使用蓝图对象
from flask import current_app
from info import redis_store

@index_bp.route('/')
def index():
    #使用日志
    current_app.logger.debug("debug")
    #设置redis键值对数据
    redis_store.set("name","laowang")

    return "index"