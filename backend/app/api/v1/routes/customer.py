from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from app.services.customer_service import CustomerService

router = APIRouter()
service = CustomerService()


@router.get("/customers", response_model=list[CustomerResponse])
async def get_customers(db: AsyncSession = Depends(get_db)):
    return await service.get_customers(db)


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await service.get_customer(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer


@router.post("/customers", response_model=CustomerResponse)
async def create_customer(
    customer: CustomerCreate,
    db: AsyncSession = Depends(get_db)
):
    return await service.create_customer(db, customer)


@router.put("/customers/{customer_id}", response_model=CustomerResponse)
async def update_customer(
    customer_id: int,
    customer: CustomerUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated = await service.update_customer(db, customer_id, customer)

    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")

    return updated


@router.delete("/customers/{customer_id}")
async def delete_customer(
    customer_id: int,
    db: AsyncSession = Depends(get_db)
):
    deleted = await service.delete_customer(db, customer_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Customer deleted successfully"}