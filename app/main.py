from fastapi import FastAPI
from sqlalchemy import text
from sqlmodel import SQLModel
from app.database.database import engine
from app.routes import checkin
from contextlib import asynccontextmanager


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(checkin.router)
