from flask import Flask, json, Response
from sqlalchemy import create_engine
from routes import init_api_routes
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello from team Hufflepuff :D'
init_api_routes(app)

db_string = os.environ.get('DATABASE_URL', None)
db = create_engine(db_string)


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
