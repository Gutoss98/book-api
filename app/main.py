from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.version import router as version_router
from app.routers.books import router as books_router

app = FastAPI(
    title="Book API",
    description="DevOps Project",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(version_router)
app.include_router(books_router)
