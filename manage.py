from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

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

    #具体储存到哪个数据库
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT,db=1)
    #session储存的数据产生后是否session_id是否需要加密
    SESSION_USE_SIGNER = True
    # 是否是永久保存
    SESSION_PERMANENT = False
    # 设置过期时长,默认过期时长31天
    PERMANENT_SESSION_LIFETIME = 86400

app = Flask(__name__)
app.config.from_object(Config)

#创建mysql数据库对象
db = SQLAlchemy(app)

#3创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port = Config.REDIS_PORT)

#4开启CSRF保护机制
CSRFProtect(app)
#5借助session调整flask.session的储存位置到redis中
Session(app)

#6创建数据库管理对象,将app交给对象管理
manager = Manager(app)

#7数据库迁移命令
Migrate(app,db)

#8添加迁移命令
manager.add_command("db",MigrateCommand)







@app.route('/')
def index():
    return



if __name__ == '__main__':
    app.run()