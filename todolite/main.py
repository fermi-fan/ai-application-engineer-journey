"""应用入口和页面路由。"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from database import create_db_and_tables, engine
from models import Todo


@asynccontextmanager
async def lifespan(_: FastAPI):
    """在应用启动时初始化数据库。"""

    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_index(request: Request) -> HTMLResponse:
    """渲染首页并显示所有待办。"""

    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"todos": todos},
    )


@app.post("/todos")
def create_todo(title: str = Form(...)) -> RedirectResponse:
    """新增一条待办。"""

    clean_title = title.strip()
    if not clean_title:
        return RedirectResponse(url="/", status_code=303)

    with Session(engine) as session:
        todo = Todo(title=clean_title)
        session.add(todo)
        session.commit()

    return RedirectResponse(url="/", status_code=303)


@app.post("/todos/{todo_id}/toggle")
def toggle_todo(todo_id: int) -> RedirectResponse:
    """切换待办的完成状态。"""

    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if todo is not None:
            todo.completed = not todo.completed
            session.add(todo)
            session.commit()

    return RedirectResponse(url="/", status_code=303)


@app.post("/todos/{todo_id}/delete")
def delete_todo(todo_id: int) -> RedirectResponse:
    """删除一条待办。"""

    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if todo is not None:
            session.delete(todo)
            session.commit()

    return RedirectResponse(url="/", status_code=303)
