from flask import Flask, json

app = Flask(__name__)
@app.route('/')
def start_service():
    message = {
        "Hufflepuff BookStore" : "Welcome to Online BookStore!!"
    }
    jasonData = json.dumps(message)
    response = Response(jasonData, status=201, mimetype='application/json')
    return response
