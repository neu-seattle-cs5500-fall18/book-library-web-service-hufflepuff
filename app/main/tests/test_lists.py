import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

def test_get_notes():
    note_id = "1"
    response = requests.get(BASE_URL + "/notes/" + note_id)
    notes = {
	  "book_id": 1,
 	  "note_id": 1,
  	  "notes": "I read this book and I loved it",
  	  "user_id": 1
	}
    assert response.json() == notes
    assert response.status_code == 200

def test_put_notes():
    payload = {
      "notes": "The book is great!"
	}
    note_id = "1"
    response = requests.put(BASE_URL + "/notes/" + note_id, json = payload)
    assert response.status_code == 200

def test_post_book():
    payload = {
  		"book_id": 2,
  		"user_id": 1,
  		"notes": "I like the book"
	}    
	response = requests.post(BASE_URL + "/notes", json = payload)

    assert response.status_code == 201

def test_delete_book():
    book_id = "1"
    response = requests.delete(BASE_URL + "/notes/" + note_id)
    assert response.status_code == 204