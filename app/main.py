from fastapi import FastAPI

from app.modules.auth.router import (
    router as auth_router,
)
from app.modules.daily_tasks.router import router as task_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(task_router)

@app.get("/")
async def health():
    return {"status": "ok"}