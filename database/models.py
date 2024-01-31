from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger)
    location = Column(String)
    food_quality = Column(String)
    food_quality_rate = Column(Integer)
    service = Column(String)
    service_rate = Column(Integer)
    ambiance = Column(String)
    ambiance_rate = Column(Integer)
    menu = Column(String)
    menu_rate = Column(Integer)
    cleanliness = Column(String)
    cleanliness_rate = Column(Integer)
    report = Column(String)
    image = Column(String)
    created_at = Column(DateTime, default=func.now())
