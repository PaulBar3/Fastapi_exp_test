import uvicorn
from fastapi import FastAPI
from app.routers import router as expenses_router
from contextlib import asynccontextmanager
from app.database import create_db



@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(expenses_router)




