from info.modules.index import index_bp
#2.使用蓝图对象
from flask import current_app

@index_bp.route('/')
def index():
    current_app.logger.debug("debug")
    return "index"