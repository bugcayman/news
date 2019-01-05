from flask import Blueprint
#1.创建蓝图对象

#让包知道wviews文件中的属土函数
#将蓝图注册到app中

passport_bp = Blueprint("index",__name__,url_prefix="/passport")
from info.modules.passport.views import *