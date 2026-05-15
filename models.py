from sqlalchemy import Column, Integer, String
from database import Base

# NOTE: Set columns mostly to NULLABLE to stop API from breaking
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    gender = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    company = Column(String, nullable=True)
    city = Column(String, nullable=True)
    title = Column(String, nullable=True)
    website = Column(String, nullable=True)