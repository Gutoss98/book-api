from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate


def get_books(db: Session):
    return db.query(Book).all()


def create_book(db: Session, book: BookCreate):
    new_book = Book(
        title=book.title,
        author=book.author
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book
