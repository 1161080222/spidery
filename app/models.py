from app import db
from datetime import datetime

class SqlEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    sql_query = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    table_info = db.Column(db.Text)
    contact = db.Column(db.String(100))
    business_domain = db.Column(db.String(100))
    business_category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sql_query = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    result = db.Column(db.Text) 