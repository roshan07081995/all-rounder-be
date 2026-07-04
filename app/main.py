from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.auth.router import (
    router as auth_router,
)
from app.modules.daily_tasks.router import router as task_router
from app.modules.monthly_tasks.router import (
    router as monthly_task_router,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(monthly_task_router)

@app.get("/")
async def health():
    return {"status": "ok"}
