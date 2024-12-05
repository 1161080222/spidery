from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SqlEntryForm(FlaskForm):
    name = StringField('SQL名称', validators=[DataRequired()])
    sql_query = TextAreaField('SQL语句', validators=[DataRequired()])
    description = TextAreaField('SQL备注')
    table_info = TextAreaField('数据表信息')
    contact = StringField('联系人')
    business_domain = StringField('业务领域')
    business_category = StringField('业务分类')
    submit = SubmitField('保存') 