from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Conta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titular: str = Field(index=True)
    numero: str = Field(default=None, index=True)
    saldo: float = Field(default=None)


#criando engine
#engine é o que mantém as conexões para o banco de dados
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
