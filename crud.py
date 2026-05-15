from sqlalchemy.orm import Session
import models
import schemas

# GET ALL
def get_customers(db: Session):
    return db.query(models.Customer).all()

# GET BY ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer)\
        .filter(models.Customer.id == customer_id)\
        .first()

# CREATE
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer

# UPDATE
def update_customer(
    db: Session,
    customer_id: int,
    customer: schemas.CustomerUpdate
):
    db_customer = get_customer(db, customer_id)

    if not db_customer:
        return None

    for key, value in customer.model_dump().items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)

    return db_customer

# DELETE
def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)

    if not db_customer:
        return None

    db.delete(db_customer)
    db.commit()

    return db_customer