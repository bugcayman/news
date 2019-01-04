from info.modules.index import index_bp
#2.使用蓝图对象
from flask import render_template
from info.models import User

@index_bp.route('/')
def index():


    return render_template("news/index.html")