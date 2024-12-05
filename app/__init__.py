from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# 初始化数据库和迁移工具
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # 创建Flask应用实例
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)  # 加载配置

    db.init_app(app)  # 初始化数据库
    migrate.init_app(app, db)  # 初始化迁移工具

    from app.routes import bp  # 导入路由
    app.register_blueprint(bp)  # 注册蓝图

    return app  # 返回应用实例 