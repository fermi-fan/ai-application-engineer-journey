# TodoLite

TodoLite 是一个适合初学者练手的 Python 全栈小项目。

它使用 FastAPI、SQLModel、SQLite 和 Jinja2 实现一个最小可运行的待办事项应用，页面通过服务端渲染返回，不依赖前端框架。

## 技术栈

- FastAPI
- SQLModel
- SQLite
- Jinja2
- Uvicorn

## 功能

- 首页展示待办列表
- 新增待办
- 切换完成状态
- 删除待办
- 使用 SQLite 持久化数据
- 使用模板页面渲染，不是纯 API

## 运行方式

1. 创建虚拟环境：

```bash
python3 -m venv .venv
```

2. 激活虚拟环境：

```bash
source .venv/bin/activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 启动项目：

```bash
uvicorn main:app --reload
```

5. 打开浏览器访问：

```text
http://127.0.0.1:8000
```

## 项目结构

```text
TodoLite/
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

## 文件职责

- `main.py`：应用入口、路由定义、页面渲染
- `models.py`：定义 Todo 数据模型
- `database.py`：配置 SQLite 连接并创建数据表
- `templates/index.html`：首页模板
- `static/style.css`：页面样式

## 学习重点

通过这个项目，你可以练习这些基础能力：

- 使用 FastAPI 编写 Web 应用
- 使用 SQLModel 操作 SQLite 数据库
- 使用 Jinja2 模板渲染页面
- 理解表单提交、重定向、数据库持久化的基本流程

## 后续可扩展方向

- 编辑待办内容
- 增加截止日期
- 按完成状态筛选
- 增加简单样式优化
- 补充单元测试
