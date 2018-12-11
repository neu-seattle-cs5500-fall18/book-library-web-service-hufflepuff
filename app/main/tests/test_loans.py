import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

all_loans = [
  {
    "book_id": 40,
    "borrowed_date": "2018-10-27",
    "loan_id": 2,
    "return_by": "2018-11-27",
    "returned_on": "2018-10-27",
    "status": "returned",
    "user": {
      "birth_year": 1995,
      "email": "krishnasai@gmail.com",
      "name": "Krishna sai",
      "phone": "+123-123-1234",
      "user_id": 2
    }
  },
  {
    "book_id": 2,
    "borrowed_date": "2018-10-27",
    "loan_id": 1,
    "return_by": "2018-10-27",
    "returned_on": "None",
    "status": "loaned out",
    "user": {
      "birth_year": 1994,
      "email": "krishna@gmail.com",
      "name": "Krishna Karanam",
      "phone": "+267-697-2488",
      "user_id": 1
    }
  }
]

def test_get_loan():
    loan_id = "1"
    response = requests.get(BASE_URL + "/loans" + loan_id)

    assert response.status_code == 200
    assert response.json() == all_loans

def test_get_loan():
    loan_id = "1"
    response = requests.get(BASE_URL + "/loans/" + loan_id)

    assert response.json() == all_books[1]
    assert response.status_code == 200

def test_put_loan():
	payload = {
        "status": "available"
    }
    loan_id = "1"
    response = requests.put(BASE_URL + "/laons/" + loan_id, json = payload)
    assert response.status_code == 200

def test_delete_book():
    loan_id = "1"
    del all_books[1]
    response = requests.delete(BASE_URL + "/loans/" + loan_id)
    assert response.status_code == 204