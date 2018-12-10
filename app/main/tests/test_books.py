import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

all_books = [
    {
        "author": "Neil Gaiman",
        "book_id": 1,
        "name": "Norse Mythology",
        "published_date": "2018-10-24",
        "status": "Borrowed",
        "subject": "Mythology"
    },
    {
        "author": "Pierce Brown",
        "book_id": 3,
        "name": "Red Rising",
        "published_date": "2013-12-31",
        "status": "Borrowed",
        "subject": "Science Fiction"
    },
    {
        "author": "Ernest Cline",
        "book_id": 2,
        "name": "Ready Player One",
        "published_date": "2011-08-16",
        "status": "loaned out",
        "subject": "Science Fiction"
    },
    {
        "author": "Rick Riordan",
        "book_id": 40,
        "name": "The Titan's Curse",
        "published_date": "2007-04-01",
        "status": "Available",
        "subject": "Fantasy Fiction"
    },
    {
        "author": "string",
        "book_id": 41,
        "name": "string",
        "published_date": "2018-12-06",
        "status": "string",
        "subject": "string"
    }
]

def test_all_books():
    response = requests.get(BASE_URL + "/books")

    assert response.json() == all_books


def test_single_book():
    book_id = "3"
    response = requests.get(BASE_URL + "/books/" + book_id)

    assert response.json() == all_books[1]

    






