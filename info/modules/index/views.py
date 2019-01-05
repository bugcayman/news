from info.modules.index import index_bp
#2.使用蓝图对象
from flask import render_template,current_app
from info.models import User

@index_bp.route('/')
def index():

    return render_template("news/index.html")

@index_bp.route('/favicon')
def get_favicon():
    """返回网站图表"""
    return current_app.send_static_file("news/info/static/news/favicon.ico")

