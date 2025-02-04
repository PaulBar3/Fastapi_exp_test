from app.database import new_session
from app.models import ExpenseModel
from app.schemas import ExpenseAddSchema, ExpenseSchema
from sqlalchemy import select


class ExpenseRepository:
    @classmethod
    async def add_expenses(cls, data: ExpenseAddSchema) -> int:
        async with new_session() as session:
            expense_dict = data.model_dump()

            expense = ExpenseModel(**expense_dict)
            session.add(expense)
            await session.flush()
            await session.commit()
            return expense.id

    @classmethod
    async def get_expenses(cls) -> list[ExpenseSchema]:
        async with new_session() as session:
            query = select(ExpenseModel)
            result = await session.execute(query)
            expense_models = result.scalars().all()
            return expense_models