from sqlalchemy import Column, Integer, Float, String
from .database import Base

class MonthlyData(Base):
    __tablename__ = "monthly_data"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String, unique=True, index=True)

    revenue = Column(Float)
    raw_cost = Column(Float)
    payroll = Column(Float)
    other_expenses = Column(Float)

    debt_payment = Column(Float)

    receivables = Column(Float)
    payables = Column(Float)
    inventory = Column(Float)

    cash = Column(Float)
