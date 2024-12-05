from app import db
from datetime import datetime

class SqlEntry(db.Model):
    # SQL条目模型
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(100), nullable=False, unique=True)  # SQL名称
    sql_query = db.Column(db.Text, nullable=False)  # SQL语句
    description = db.Column(db.Text)  # SQL备注
    table_info = db.Column(db.Text)  # 数据表信息
    contact = db.Column(db.String(100))  # 联系人
    business_domain = db.Column(db.String(100))  # 业务领域
    business_category = db.Column(db.String(100))  # 业务分类
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # 更新时间

class Query(db.Model):
    # 查询记录模型
    id = db.Column(db.Integer, primary_key=True)  # 主键
    sql_query = db.Column(db.Text, nullable=False)  # SQL语句
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # 查询时间
    result = db.Column(db.Text)  # 查询结果 