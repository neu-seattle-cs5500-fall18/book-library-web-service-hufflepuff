import json
import requests

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

response = requests.get(BASE_URL + "/books")
print(response)
#print(response.json())
print(json.dumps(response.json(), indent = 4))
