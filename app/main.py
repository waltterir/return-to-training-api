from fastapi import FastAPI
from sqlalchemy import text
from sqlmodel import SQLModel
from app.database.database import engine
from app.models.models import User, CheckIn, Training, Recommendation

SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db": "connected"}