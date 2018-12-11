import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

def test_get_user():
    user = {
      "birth_year": 1994,
      "email": "divya@gmail.com",
      "name": "Divya",
      "phone": "6303138860",
      "user_id": 41
    }
    user_id = 41
    response = requests.get(BASE_URL + "/users"+user_id)

    assert response.json() == user


def test_get_user_lists():
    user_id = 1
    response = requests.get(BASE_URL + "/users/" + user_id)

    assert response.status_code == 200


def test_get_user_notes():
    user_id = 1
    book_id = 1
    response = requests.get(BASE_URL + "/users/"+user_id "/books/" + book_id+ "/notes")

    assert response.status_code == 200


def test_user_get_loans():
    user_id = 1
    book_id = 1
    response = requests.get(BASE_URL + "/users/"+user_id+"/loans")

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
