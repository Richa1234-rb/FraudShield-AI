from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.config.settings import settings
from app.database.init_db import init_db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Powered Financial Fraud Detection System",
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "message": f"🚀 {settings.APP_NAME} Backend Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }