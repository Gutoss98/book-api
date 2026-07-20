from fastapi import FastAPI

from app.database import Base, engine
from app.routers.books import router as books_router
from app.routers.health import router as health_router
from app.routers.version import router as version_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    version="1.0.0",
    description="DevOps project"
)

app.include_router(health_router)
app.include_router(version_router)
app.include_router(books_router)
