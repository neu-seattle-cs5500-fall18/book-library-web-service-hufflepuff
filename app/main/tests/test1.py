import json
import requests

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

payload = { "status": "available" }
book_id = "46"
response = requests.put(BASE_URL + "/books/" + book_id, json = payload)
print(response.status_code)
#print(response.json())
print(json.dumps(response.json(), indent = 4))