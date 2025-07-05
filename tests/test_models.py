import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from models import Book, Library


@pytest.fixture
def sample_book():
    return Book(author="John Smith", title="Python 101", book_id=1)


@pytest.fixture
def sample_library():
    return Library(name="Central Library")


def test_book_creation(sample_book):
    assert sample_book.author == "John Smith"
    assert sample_book.title == "Python 101"
    assert sample_book.book_id == 1


def test_library_creation(sample_library):
    assert sample_library.name == "Central Library"
    assert sample_library.books == []


def test_add_book(sample_library, sample_book):
    sample_library.add_book(sample_book)
    assert len(sample_library.books) == 1
    assert sample_library.books[0].title == "Python 101"


def test_remove_book(sample_library, sample_book):
    sample_library.add_book(sample_book)
    sample_library.remove_book_by_id(1)
    assert len(sample_library.books) == 0


def test_remove_nonexistent_book(sample_library):
    sample_library.remove_book_by_id(999)
    assert sample_library.books == []


def test_multiple_books(sample_library):
    books = [Book("A", "Book A", 1), Book("B", "Book B", 2)]
    for b in books:
        sample_library.add_book(b)
    assert len(sample_library.books) == 2
