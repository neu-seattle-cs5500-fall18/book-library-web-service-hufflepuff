from .data_provider_service import DataProviderService
from flask import abort, jsonify
import os

db_string = os.environ.get('DATABASE_URL', None)
DATA_PROVIDER = DataProviderService(db_string)


def initialize_database():
    DATA_PROVIDER.init_database()


def get_users():
    current_users = DATA_PROVIDER.get_users()
    if current_users:
        return jsonify(current_users)
    else:
        #
        # In case we did not find any users
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def add_books():
    name = request.form["name"]
    author = request.form["author"]
    subject = request.form["subject"]
    status = request.form["status"]
    published_date = request.form["published_date"]

    new_book_id = DATA_PROVIDER.add_books(name=name,
                                          author=author,
                                          subject=subject,
                                          status=status,
                                          published_date=published_date)

    return jsonify({
        "id": new_book_id,
        "name": name,
        "author": author,
        "subject": subject,
        "status": status,
        "published_date": published_date
    })
