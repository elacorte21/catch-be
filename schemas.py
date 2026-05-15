from typing import Optional, List
from pydantic import BaseModel, ConfigDict

class CustomerBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    ip_address: Optional[str] = None
    company: Optional[str] = None
    city: Optional[str] = None
    title: Optional[str] = None
    website: Optional[str] = None

class CustomerList(BaseModel):
    page: int
    per_page: int
    total: int
    items: List[Customer]

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)