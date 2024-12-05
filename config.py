import os

class Config:
    # Flask应用的配置类
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'  # 用于会话和CSRF保护的密钥
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///spidery.db'  # 数据库连接URI，默认为SQLite数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用对象修改追踪