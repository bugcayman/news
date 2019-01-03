from info.modules.index import index_bp
#2.使用蓝图对象
from flask import current_app

@index_bp.route('/')
def index():
    #使用日志
    current_app.logger.debug("debug")

    return "index"