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
        return current_books
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def search_books(author, subject, published_date_from, published_date_to):
    current_books = DATA_PROVIDER.search_books(author, subject, published_date_from, published_date_to)
    if current_books:
        return current_books
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_book(book_id):
    current_book = DATA_PROVIDER.get_book(book_id)
    if current_book:
        return current_book
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def put_book(book):
    current_book = DATA_PROVIDER.put_book(book)
    if current_book:
        return current_book
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_book(book):
    status = DATA_PROVIDER.delete_book(book)
    if status:
        return status
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def add_books(book):
    new_book = DATA_PROVIDER.add_book(book)
    return new_book


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
