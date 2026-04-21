"""定义待办数据模型。"""

from typing import Optional

from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    """表示一条待办事项。"""

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    completed: bool = False
