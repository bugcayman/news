from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


#0创建配置类
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

app = Flask(__name__)
app.config.from_object(Config)

#创建mysql数据库对象
db = SQLAlchemy(app)

#3创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port = Config.REDIS_PORT)
CSRFProtect(app)

@app.route('/')
def index():
    return


if __name__ == '__main__':
    app.run()