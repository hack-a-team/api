"""
Provides Pydantic schemas for the datamodels
"""
from datetime import datetime
from pydantic import BaseModel, Schema


class AlertBase(BaseModel):
    """
    Alert is a simple incident alert at the Port
    """

    kind: str
    transaction: str = None


class AlertCreate(AlertBase):
    """
    AlertCreate is a proxy class for alert creation
    """


class Alert(AlertBase):
    """
    Alert represents an alert message about an event at the port
    """

    id: int
    timestamp: datetime

    def __str__(self):
        return f"Alert: id={self.id}, kind={self.kind}, timestamp={self.timestamp}"

    class Config:
        """
        Config defines metadata for Alert
        """

        orm_mode = True


class CargoBase(BaseModel):
    """
    CargoBase defines de schema shared by all Cargo items
    """

    location: str
    latitude: float
    longitude: float
    kind: str


class CargoCreate(CargoBase):
    """
    CargoCreate is a proxy class for cargo creation
    """


class Cargo(CargoBase):
    """
    Cargo represents a cargo at the port
    """

    id: int

    class Config:
        """
        Defines metadata for cargo
        """

        orm_mode = True
