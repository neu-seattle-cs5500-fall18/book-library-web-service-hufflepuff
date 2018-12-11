import json
import requests
import pytest

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

def test_post_admin():
    loan_id = "1"
    response = requests.post(BASE_URL + "/admin/remind/" + loan_id)

    assert response.status_code == 201