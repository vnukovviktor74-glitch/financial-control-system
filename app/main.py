from fastapi import FastAPI
from app.database import engine, Base
from app import models

app = FastAPI(title="Financial Control System")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}
