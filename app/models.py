from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class FinancialData(Base):
    __tablename__ = "financial_data"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float)
    raw_cost = Column(Float)
    operating_expenses = Column(Float)
    debt_service = Column(Float)
