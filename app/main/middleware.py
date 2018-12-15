from .data_provider_service import DataProviderService
from flask import abort, jsonify, make_response, request, url_for
import os

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


def get_loans():
    current_loans = DATA_PROVIDER.get_loans()
    if current_loans:
        return current_loans
    else:
        #
        # In case we did not find any loans
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_userloans(user_id):
    current_loans = DATA_PROVIDER.get_userloans(user_id)
    if current_loans:
        return current_loans
    else:
        #
        # In case we did not find any loans
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def remind_user(user, book, return_by):
    status = DATA_PROVIDER.remind_user(user, book, return_by)
    if status:
        return status
    else:
        #
        # In case we did not find any loans
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_userlists(user_id):
    current_lists = DATA_PROVIDER.get_userlists(user_id)
    if current_lists:
        return current_lists
    else:
        #
        # In case we did not find any lists
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


def get_user(user_id):
    current_user = DATA_PROVIDER.get_user(user_id)
    if current_user:
        return current_user
    else:
        #
        # In case we did not find any user
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_note(note_id):
    current_notes = DATA_PROVIDER.get_note(note_id)
    if current_notes:
        return current_notes
    else:
        #
        # In case we did not find any note
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_loan(loan_id):
    current_loan = DATA_PROVIDER.get_loan(loan_id)
    if current_loan:
        return current_loan
    else:
        #
        # In case we did not find any loan
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_list(list_id):
    current_list = DATA_PROVIDER.get_list(list_id)
    if current_list:
        return current_list
    else:
        #
        # In case we did not find any list
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def get_list_object(list_id):
    current_list = DATA_PROVIDER.get_list_object(list_id)
    if current_list:
        return current_list
    else:
        #
        # In case we did not find any list
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def find_note(user_id, book_id):
    current_notes = DATA_PROVIDER.find_note(user_id, book_id)
    if current_notes:
        return current_notes
    else:
        #
        # In case we did not find any user
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


def put_user(user):
    current_user = DATA_PROVIDER.put_user(user)
    if current_user:
        return current_user
    else:
        #
        # In case we did not find any user
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def put_note(note):
    current_note = DATA_PROVIDER.put_note(note)
    if current_note:
        return current_note
    else:
        #
        # In case we did not find any user
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def put_loan(loan):
    current_loan = DATA_PROVIDER.put_loan(loan)
    if current_loan:
        return current_loan
    else:
        #
        # In case we did not find any loan
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def put_list(the_list, books):
    current_list = DATA_PROVIDER.put_list(the_list, books)
    if current_list:
        return current_list
    else:
        #
        # In case we did not find any list
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_book(book_id):
    status = DATA_PROVIDER.delete_book(book_id)
    if status:
        return status
    else:
        #
        # In case we did not find any books
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_user(user_id):
    status = DATA_PROVIDER.delete_user(user_id)
    if status:
        return status
    else:
        #
        # In case we did not find any users
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_note(note_id):
    status = DATA_PROVIDER.delete_note(note_id)
    if status:
        return status
    else:
        #
        # In case we did not find any notes
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_loan(loan_id):
    status = DATA_PROVIDER.delete_loan(loan_id)
    if status:
        return status
    else:
        #
        # In case we did not find any loan
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def delete_list(list_id):
    status = DATA_PROVIDER.delete_list(list_id)
    if status:
        return status
    else:
        #
        # In case we did not find any list
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def add_books(book):
    new_book = DATA_PROVIDER.add_book(book)
    return new_book


def add_users(user):
    new_user = DATA_PROVIDER.add_user(user)
    return new_user


def add_notes(note):
    new_note = DATA_PROVIDER.add_note(note)
    return new_note


def add_loans(loan):
    new_loan = DATA_PROVIDER.add_loan(loan)
    return new_loan


def add_lists(add_list, book_ids):
    new_list = DATA_PROVIDER.add_list(add_list, book_ids)
    return new_list
