from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models import Query, SqlEntry
from app import db
import sqlite3
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    sql_entries = SqlEntry.query.order_by(SqlEntry.created_at.desc()).all()
    return render_template('index.html', sql_entries=sql_entries)

@bp.route('/execute', methods=['POST'])
def execute_query():
    sql = request.json.get('query')
    try:
        conn = sqlite3.connect('spidery.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        
        query = Query(sql_query=sql, result=str(results))
        db.session.add(query)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'columns': columns,
            'data': results
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@bp.route('/sql_entry/add', methods=['POST'])
def add_sql_entry():
    try:
        data = request.json
        entry = SqlEntry(
            name=data['name'],
            sql_query=data['sql_query'],
            description=data.get('description', ''),
            table_info=data.get('table_info', ''),
            contact=data.get('contact', ''),
            business_domain=data.get('business_domain', ''),
            business_category=data.get('business_category', '')
        )
        db.session.add(entry)
        db.session.commit()
        return jsonify({'status': 'success', 'id': entry.id})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@bp.route('/sql_entry/<int:id>', methods=['PUT'])
def update_sql_entry(id):
    try:
        entry = SqlEntry.query.get_or_404(id)
        data = request.json
        entry.name = data.get('name', entry.name)
        entry.sql_query = data.get('sql_query', entry.sql_query)
        entry.description = data.get('description', entry.description)
        entry.table_info = data.get('table_info', entry.table_info)
        entry.contact = data.get('contact', entry.contact)
        entry.business_domain = data.get('business_domain', entry.business_domain)
        entry.business_category = data.get('business_category', entry.business_category)
        entry.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@bp.route('/sql_entry/<int:id>', methods=['DELETE'])
def delete_sql_entry(id):
    try:
        entry = SqlEntry.query.get_or_404(id)
        db.session.delete(entry)
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@bp.route('/sql_entry/<int:id>', methods=['GET'])
def get_sql_entry(id):
    try:
        entry = SqlEntry.query.get_or_404(id)
        return jsonify({
            'status': 'success',
            'data': {
                'id': entry.id,
                'name': entry.name,
                'sql_query': entry.sql_query,
                'description': entry.description,
                'table_info': entry.table_info,
                'contact': entry.contact,
                'business_domain': entry.business_domain,
                'business_category': entry.business_category
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400 