from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Hello World
@app.get("/")
async def root():
    return {"message": "Hello World"}


# GET ALL CUSTOMERS
@app.get("/customers", response_model=schemas.CustomerList)
def get_customers(
    per_page: int = Query(10, ge=1, le=100),
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db)
):

    skip = (page - 1) * per_page

    total = db.query(models.Customer).count()

    customers = (
        db.query(models.Customer)
        .offset(skip)
        .limit(per_page)
        .all()
    )

    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": customers
    }


# GET CUSTOMER BY ID
@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):

    customer = crud.get_customer(db, customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


# CREATE CUSTOMER
@app.post("/customers", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):

    return crud.create_customer(db, customer)


# UPDATE CUSTOMER
@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int,
                    customer: schemas.CustomerUpdate,
                    db: Session = Depends(get_db)):

    updated_customer = crud.update_customer(
        db,
        customer_id,
        customer
    )

    if not updated_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return updated_customer


# DELETE CUSTOMER
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int,
                    db: Session = Depends(get_db)):

    deleted_customer = crud.delete_customer(
        db,
        customer_id
    )

    if not deleted_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }