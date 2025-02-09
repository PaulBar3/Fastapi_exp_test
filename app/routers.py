from typing import Annotated
from fastapi import APIRouter, Depends
from app.reposetory import ExpenseRepository
from app.schemas import ExpenseSchema, ExpenseAddSchema
from fastapi.exceptions import HTTPValidationError


router = APIRouter(prefix="/expenses", tags=["Расходы"])


@router.get("/")
async def get_expenses() -> list[ExpenseSchema]:
    expense = await ExpenseRepository.get_expenses()
    return expense


@router.post("/", responses={
    422:{
        "description": "Невалидные данные",
        "content": HTTPValidationError
    }
})
async def add_expense(
    expense: Annotated[ExpenseAddSchema, Depends(ExpenseSchema)]) -> dict:
    expense_id = await ExpenseRepository.add_expenses(expense)
    return {"ok": 'Запись успешно добавлена', "id": expense_id}
