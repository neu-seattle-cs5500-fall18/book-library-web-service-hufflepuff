from flask import Flask, json, Response
from sqlalchemy import create_engine
# import routes
from .routes import init_api_routes
import os
from flask_cors import CORS


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello from team Hufflepuff :D'
CORS(app)
init_api_routes(app)


@app.route('/')
def start_service():
    message = {
        "store": "Welcome to Online BookStore!!"
    }
    jasonData = json.dumps(message)
    response = Response(jasonData, status=201, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
