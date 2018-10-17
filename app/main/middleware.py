from .data_provider_service import DataProviderService
from flask import abort, jsonify, make_response, request, url_for
import os

# db_string = os.environ.get('DATABASE_URL', None)
db_string = os.environ.get('DATABASE_URL', None)
DATA_PROVIDER = DataProviderService(db_string)


def initialize_database():
    DATA_PROVIDER.init_database()

# initialize_database()


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


def get_user(user_id):
    current_users = ["hello"]
    if user_id == "12":
        return current_users, 200
    else:
        #
        # In case we did not find any users
        # we send HTTP 404 - Not Found error to the client
        #
        return current_users, 204


def get_books():
    current_books = DATA_PROVIDER.get_books()
    if current_books:
        return jsonify(current_books)
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def add_books():
    data = request.json
    print(data)
    name = data['name']
    author = data['author']
    subject = data['subject']
    status = data['status']
    published_date = data['published_date']

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


def add_users():
    data = request.json
    name = data['name']
    email = data['email']
    phone = data['phone']
    birth_year = data['birth_year']

    new_book_id = DATA_PROVIDER.add_users(name=name,
                                          email=email,
                                          phone=phone,
                                          birth_year=birth_year)

    return jsonify({
        "id": new_book_id,
        "name": name,
        "email": email,
        "phone": phone,
        "birth_year": birth_year
    })
