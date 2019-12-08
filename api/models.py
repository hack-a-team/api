"""
Provides SQLAlchemy models.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

from database import Base


class Alert(Base):
    """
    Alert is an SQLAlchemy model for a minor incident report at the port
    """

    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    kind = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transaction = Column(String)


class Cargo(Base):
    """
    Cargo is an model for a cargo at the port
    """

    __tablename__ = "cargos"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    kind = Column(String)
