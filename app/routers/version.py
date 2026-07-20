from fastapi import APIRouter
from app.version import VERSION

router = APIRouter(tags=["Version"])


@router.get("/version")
def version():
    return {
        "version": VERSION
    }
