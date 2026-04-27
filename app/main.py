from fastapi import FastAPI
from sqlalchemy import text
from app.database.database import engine

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db": "connected"}