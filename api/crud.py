from sqlalchemy.orm import Session
from pyrbi import PyRBI

import config
import models
import schemas


def get_alerts(db: Session, skip: int = 0, limit: int = 0):
    """
    Lists all alerts
    """
    return db.query(models.Alert).offset(skip).limit(limit).all()


def create_alert(db: Session, alert: schemas.AlertCreate):
    """
    Creates a new alert
    """

    # Register the alert in the ledger
    rbi = PyRBI(config.BLOCK_USERNAME, config.BLOCK_PASSWORD)
    data = rbi.put_data(str(alert), config.ALERT_WALLET_ADDRESS, config.ALERT_WALLET_PK)
    transaction = data["data"]

    print(transaction)

    # Register the alert in the database
    db_alert = models.Alert(kind=alert.kind, transaction=transaction)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    return db_alert


def create_cargo(db: Session, cargo: schemas.CargoCreate):
    """
    Creates a new cargo item
    """
    db_cargo = models.Cargo(
        location=cargo.location,
        latitude=cargo.latitude,
        longitude=cargo.longitude,
        type=cargo.type,
    )
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)

    return db_cargo


def get_cargos(db: Session, skip: int = 0, limit: int = 0):
    """
    Lists all cargo items
    """
    return db.query(models.Cargo).offset(skip).limit(limit).all()
