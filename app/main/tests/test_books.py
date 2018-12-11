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
  },
  {
    "author": "Robin Sharma",
    "book_id": 42,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2018-12-10",
    "status": "Available",
    "subject": "Phylosophy"
  },
  {
    "author": "Robin Sharma",
    "book_id": 43,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2017-12-10",
    "status": "Available",
    "subject": "Phylosophy"
  },
  {
    "author": "Robin Sharma",
    "book_id": 44,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2017-12-10",
    "status": "Available",
    "subject": "Phylosophy"
  },
  {
    "author": "Robin Sharma",
    "book_id": 45,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2017-12-10",
    "status": "Available",
    "subject": "Phylosophy"
  },
  {
    "author": "Robin Sharma",
    "book_id": 46,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2017-12-10",
    "status": "Available",
    "subject": "Phylosophy"
  }
]

book_created_response = {
    "author": "Robin Sharma",
    "book_id": 42,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2018-12-10",
    "status": "Available",
    "subject": "Phylosophy"
}

def test_get_all_books():
    response = requests.get(BASE_URL + "/books")

    assert response.json() == all_books


def test_get_book():
    book_id = "3"
    response = requests.get(BASE_URL + "/books/" + book_id)

    assert response.json() == all_books[1]
    assert response.status_code == 200


def test_post_book():
    payload = {
      "name": "The Monk Who Sold His Ferrari",
      "author": "Robin Sharma",
      "subject": "Phylosophy",
      "status": "Available",
      "published_date": "2017-12-10T21:33:18.112Z"
    }
    response = requests.post(BASE_URL + "/books", json = payload)

    all_books.append({
    "author": "Robin Sharma",
    "book_id": 60,
    "name": "The Monk Who Sold His Ferrari",
    "published_date": "2018-12-10",
    "status": "Available",
    "subject": "Phylosophy"
    })
    assert response.json() == book_created_response


def test_delete_book():
    book_id = "60"
    del all_books[10]
    response = requests.delete(BASE_URL + "/books/" + book_id)
    assert response.status_code == 204


def test_post_search_book():
    payload = { "author": "Neil Gaiman" }
    response = requests.post(BASE_URL + "/books/search", json = payload)

    assert response.json() == all_books[0]

def test_put_book():
    payload = {
        "status": "loaned out"
    }
    book_id = "46"
    response = requests.put(BASE_URL + "/books/" + book_id, json = payload)
    assert response.status_code == 200
