from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models import Query, SqlEntry
from app import db
from app.forms import SqlEntryForm  # 导入表单
import sqlite3
from datetime import datetime

bp = Blueprint('main', __name__)  # 创建蓝图

@bp.route('/')
def index():
    # 首页路由，显示所有SQL条目
    sql_entries = SqlEntry.query.order_by(SqlEntry.created_at.desc()).all()  # 获取所有SQL条目
    return render_template('index.html', sql_entries=sql_entries)  # 渲染模板

@bp.route('/sql_entry/add', methods=['GET', 'POST'])
def add_sql_entry():
    # 新建SQL条目路由
    form = SqlEntryForm()  # 创建表单实例
    if form.validate_on_submit():  # 如果表单提交有效
        entry = SqlEntry(
            name=form.name.data,
            sql_query=form.sql_query.data,
            description=form.description.data,
            table_info=form.table_info.data,
            contact=form.contact.data,
            business_domain=form.business_domain.data,
            business_category=form.business_category.data
        )
        db.session.add(entry)  # 添加条目到数据库
        db.session.commit()  # 提交更改
        return redirect(url_for('main.index'))  # 重定向到首页
    return render_template('sql_entry_form.html', form=form)  # 渲染新建SQL表单模板

@bp.route('/sql_entry/<int:id>/edit', methods=['GET', 'POST'])
def edit_sql_entry(id):
    # 编辑SQL条目路由
    entry = SqlEntry.query.get_or_404(id)  # 获取指定ID的SQL条目
    form = SqlEntryForm(obj=entry)  # 创建表单实例并填充数据
    if form.validate_on_submit():  # 如果表单提交有效
        entry.name = form.name.data
        entry.sql_query = form.sql_query.data
        entry.description = form.description.data
        entry.table_info = form.table_info.data
        entry.contact = form.contact.data
        entry.business_domain = form.business_domain.data
        entry.business_category = form.business_category.data
        db.session.commit()  # 提交更改
        return redirect(url_for('main.index'))  # 重定向到首页
    return render_template('sql_entry_form.html', form=form, entry=entry)  # 渲染编辑SQL表单模板

@bp.route('/execute', methods=['POST'])
def execute_query():
    # 执行SQL查询路由
    sql = request.json.get('query')  # 获取SQL查询
    try:
        conn = sqlite3.connect('spidery.db')  # 连接数据库
        cursor = conn.cursor()
        cursor.execute(sql)  # 执行SQL查询
        results = cursor.fetchall()  # 获取结果
        columns = [description[0] for description in cursor.description]  # 获取列名
        
        query = Query(sql_query=sql, result=str(results))  # 创建查询记录
        db.session.add(query)  # 添加查询记录到数据库
        db.session.commit()  # 提交更改
        
        return jsonify({
            'status': 'success',
            'columns': columns,
            'data': results
        })  # 返回成功响应
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400  # 返回错误响应

@bp.route('/sql_entry/<int:id>', methods=['DELETE'])
def delete_sql_entry(id):
    # 删除SQL条目路由
    try:
        entry = SqlEntry.query.get_or_404(id)  # 获取指定ID的SQL条目
        db.session.delete(entry)  # 删除条目
        db.session.commit()  # 提交更改
        return jsonify({'status': 'success'})  # 返回成功响应
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400  # 返回错误响应

@bp.route('/sql_entry/<int:id>', methods=['GET'])
def get_sql_entry(id):
    # 获取SQL条目详情路由
    try:
        entry = SqlEntry.query.get_or_404(id)  # 获取指定ID的SQL条目
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
        })  # 返回成功响应
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400  # 返回错误响应
  