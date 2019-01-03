from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db


app = create_app("development")
#6创建数据库管理对象,将app交给对象管理
manager = Manager(app)

#7数据库迁移命令
Migrate(app,db)

#8添加迁移命令
manager.add_command("db",MigrateCommand)



if __name__ == '__main__':
    manager.run()