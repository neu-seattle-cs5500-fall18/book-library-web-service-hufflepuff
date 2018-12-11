import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

def test_get_lists():
    list_id = "1"
    response = requests.get(BASE_URL + "/lists/" + note_id)

    assert response.status_code == 200

def test_put_lists():
    payload = {
      "list_name": "Classics"
    }
    list_id = "1"
    response = requests.put(BASE_URL + "/lists/" + list_id, json = payload)
    assert response.status_code == 200

def test_delete_lists():
    list_id = "1"
    response = requests.delete(BASE_URL + "/lists/" + list_id)
    assert response.status_code == 204