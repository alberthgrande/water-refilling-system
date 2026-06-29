from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self):
        self.repo = CustomerRepository()

    async def get_customers(self, db: AsyncSession):
        return await self.repo.get_all(db)

    async def get_customer(self, db: AsyncSession, customer_id: int):
        return await self.repo.get_by_id(db, customer_id)

    async def create_customer(self, db: AsyncSession, customer):
        return await self.repo.create(db, customer)

    async def update_customer(self, db: AsyncSession, customer_id: int, customer):
        return await self.repo.update(db, customer_id, customer)

    async def delete_customer(self, db: AsyncSession, customer_id: int):
        return await self.repo.delete(db, customer_id)