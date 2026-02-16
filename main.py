from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models import MonthlyData

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "Financial Control System running"}

@app.post("/add-month")
def add_month(data: dict, db: Session = Depends(get_db)):
    month = MonthlyData(**data)
    db.add(month)
    db.commit()
    return {"message": "Month added"}

@app.get("/months")
def get_months(db: Session = Depends(get_db)):
    return db.query(MonthlyData).all()
