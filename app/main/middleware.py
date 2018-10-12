from .data_provider_service import DataProviderService
from flask import abort, jsonify
import os

db_string = os.environ.get('DATABASE_URL', "postgres://vywhwbzvzxprkq:2f7083fed0106103e25ce5300750f5a8af50678ae11710731e61692e7deab729@ec2-54-225-76-201.compute-1.amazonaws.com:5432/d58h3832oj43d6")
DATA_PROVIDER = DataProviderService(db_string)


def initialize_database():
    DATA_PROVIDER.init_database()


def get_users():
    current_users = DATA_PROVIDER.get_users()
    if current_users:
        return jsonify({"users": current_users})
    else:
        #
        # In case we did not find any users
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)
