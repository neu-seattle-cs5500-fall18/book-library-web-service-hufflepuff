from .data_provider_service import DataProviderService
from flask import abort
import os

db_string = os.environ.get('DATABASE_URL', None)
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
