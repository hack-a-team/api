from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
import uvicorn

import crud
import models
import schemas
from database import SessionLocal, engine

origins = [
    "http://94f37516.ngrok.io",
    "https://94f37516.ngrok.io",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8100",
    "http://localhost:3001",
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    """
    Handles DB conn
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    """
    the root!
    """
    return {"message": "Welcome home"}


@app.get("/prediction")
def prediction(date=None):
    """
    prediction returns the probability of an accident happening
    """
    if date:
        return {"prediction": 30}
    return {"prediction": 23}


@app.post("/alerts/", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.create_alert(db=db, alert=alert)


@app.get("/alerts/", response_model=List[schemas.Alert])
def read_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lists all the alerts defined in the database
    """
    alerts = crud.get_alerts(db, skip=skip, limit=limit)
    return alerts


@app.post("/cargos/", response_model=schemas.Cargo)
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    """
    creates a new cargo item
    """
    return crud.create_cargo(db=db, cargo=cargo)


@app.get("/cargos/", response_model=List[schemas.Cargo])
def read_cargos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lists all the cargos defined in the database
    """
    cargos = crud.get_cargos(db, skip=skip, limit=limit)
    return cargos


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")
