from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from data import create_db_and_tables, Conta, SessionDep

from fastapi import Depends, FastAPI, HTTPException, status, Query, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Union

from controllers import auth

app = FastAPI()
app.include_router(auth.router)


class ContaBancaria(BaseModel):
    id: int
    titular: Union[str, None] = None
    numero: str
    saldo: Union[float, None] = None


@app.post("/conta/")
def create_item(conta: ContaBancaria):
    return conta