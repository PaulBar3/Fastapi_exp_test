from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime)


class ExpenseModel(Base):
    __tablename__ = "expenses"

    name: Mapped[str]
    amount: Mapped[float]
    comment: Mapped[str]
