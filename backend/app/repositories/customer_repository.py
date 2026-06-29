from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.customer import Customer


class CustomerRepository:

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Customer))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, customer_id: int):
        result = await db.execute(
            select(Customer).where(Customer.id == customer_id)
        )
        return result.scalars().first()

    async def create(self, db: AsyncSession, customer):
        new_customer = Customer(**customer.model_dump())

        db.add(new_customer)
        await db.commit()
        await db.refresh(new_customer)

        return new_customer

    async def update(self, db: AsyncSession, customer_id: int, customer):
        result = await db.execute(
            select(Customer).where(Customer.id == customer_id)
        )
        db_customer = result.scalars().first()

        if not db_customer:
            return None

        update_data = customer.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_customer, key, value)

        await db.commit()
        await db.refresh(db_customer)

        return db_customer

    async def delete(self, db: AsyncSession, customer_id: int):
        result = await db.execute(
            select(Customer).where(Customer.id == customer_id)
        )
        db_customer = result.scalars().first()

        if not db_customer:
            return None

        await db.delete(db_customer)
        await db.commit()

        return True