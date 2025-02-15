from pydantic import BaseModel, Field
from datetime import datetime


class ExpenseSchema(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    amount: int = Field(ge=1)
    comment: str = Field(min_length=3, max_length=100)


class ExpenseAddSchema(ExpenseSchema):
    id: int
    created_at: datetime = datetime.now()


class ExpenseUpdateSchema(ExpenseSchema):
    pass