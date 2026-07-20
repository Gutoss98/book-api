from fastapi import APIRouter
from app.models.book import Book
from app.services.book_service import get_all_books, add_book

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("")
def get_books():
    return get_all_books()


@router.post("")
def create_book(book: Book):
    return add_book(book)
