from app.models.book import Book

books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin"),
    Book(id=2, title="The Phoenix Project", author="Gene Kim"),
]


def get_all_books():
    return books


def add_book(book: Book):
    books.append(book)
    return book
