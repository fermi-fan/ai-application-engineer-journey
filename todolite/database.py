"""管理数据库连接和建表。"""

from sqlmodel import SQLModel, create_engine


sqlite_file_name = "todolite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def create_db_and_tables() -> None:
    """创建项目需要的数据库表。"""

    SQLModel.metadata.create_all(engine)
