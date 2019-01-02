from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from config import config_dict


app = Flask(__name__)

#根据development建获取对应的配置类名
config_class = config_dict["development"]

app.config.from_object(config_class)

#创建mysql数据库对象
db = SQLAlchemy(app)

#3创建redis数据库对象
redis_store = StrictRedis(host=config_class.REDIS_HOST, port = config_class.REDIS_PORT)

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
    return "index"



if __name__ == '__main__':
    manager.run()