from pydantic import BaseModel
from typing import Optional

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerResponse(CustomerCreate):
    id: int

    model_config = {
        "from_attributes": True
    }