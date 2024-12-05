# Spidery SQL管理器

Spidery是一个基于Flask的SQL管理应用，允许用户创建、编辑和执行SQL查询。该应用提供了一个简单的Web界面，用户可以通过该界面管理SQL条目。

## 功能

- **新建SQL条目**：用户可以创建新的SQL条目并保存到数据库中。
- **编辑SQL条目**：用户可以修改现有的SQL条目。
- **删除SQL条目**：用户可以删除不再需要的SQL条目。
- **执行SQL查询**：用户可以执行SQL查询并查看结果。
- **查看SQL条目详情**：用户可以查看每个SQL条目的详细信息。

## 技术栈

- **Flask**：用于构建Web应用的Python框架。
- **Flask-SQLAlchemy**：用于数据库操作的ORM工具。
- **Flask-Migrate**：用于数据库迁移的工具。
- **Flask-WTF**：用于表单处理和CSRF保护。
- **SQLite**：轻量级数据库，作为默认数据库。

## 项目结构

```
spidery/
├── app/
│   ├── __init__.py          # 应用初始化文件
│   ├── static/               # 静态文件（CSS、JS等）
│   │   └── style.css         # 样式文件
│   ├── templates/            # 模板文件
│   │   ├── base.html         # 基础模板
│   │   ├── index.html        # 首页模板
│   │   └── sql_entry_form.html # 新建和编辑SQL条目模板
│   ├── models.py             # 数据模型定义
│   ├── routes.py             # 路由处理
│   ├── forms.py              # 表单处理
│   └── utils.py              # 工具函数（如有需要）
├── config.py                  # 配置文件
├── run.py                     # 启动应用
└── requirements.txt           # 项目依赖
```

## 安装

1. 克隆该仓库：

   ```bash
   git clone <repository-url>
   cd spidery
   ```

2. 创建并激活虚拟环境：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 初始化数据库：

   ```bash
   python run.py
   ```

5. 运行应用：

   ```bash
   python run.py
   ```

6. 打开浏览器，访问 `http://localhost:5000`。

## 使用

- 在首页，您可以查看所有SQL条目。
- 点击“新建SQL”按钮以创建新的SQL条目。
- 点击“编辑”按钮以修改现有条目。
- 点击“删除”按钮以��除条目。
- 点击SQL条目以查看详细信息。

## 代码示例

以下是`app/templates/index.html`的部分代码示例：

```html
<td class="sql-name">{{ entry.name }}</td>
<td class="sql-content-cell">
    <div class="sql-preview" onclick="showDetails({{ entry.id }})">
        <pre><code class="sql">{{ entry.sql_query[:150] + '...' if entry.sql_query|length > 150 else entry.sql_query }}</code></pre>
        <span class="view-more" style="display: none;">点击查看更多</span>
    </div>
</td>
```

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证

该项目使用MIT许可证。请查看LICENSE文件以获取更多信息。
