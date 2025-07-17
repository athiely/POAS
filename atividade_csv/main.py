from fastapi import FastAPI, Depends 
from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from contextlib import asynccontextmanager
from models import Pedido

url = "sqlite:///banco.db"
engine = create_engine

def get_session():

    yield Session

def create_db():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

