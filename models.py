from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    author: str
    title: str
    book_id: int


@dataclass
class Library:
    name: str
    books: List[Book] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book_by_id(self, book_id: int):
        self.books = [book for book in self.books if book.book_id != book_id]

