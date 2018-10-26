from .middleware import initialize_database as init_db
from flask_restplus import Api, Resource, fields
from flask import abort, jsonify, make_response, request, url_for

from .models.user import User
from .models.library import Library
from .models.notes import Notes
from .models.loan import Loan
from .models.list import List
from .models.listitem import Listitem

from .middleware import get_books
from .middleware import get_users
from .middleware import get_loans
from .middleware import get_userloans
from .middleware import search_books
from .middleware import find_note
from .middleware import delete_book
from .middleware import delete_user
from .middleware import delete_note
from .middleware import delete_loan
from .middleware import put_book
from .middleware import put_user
from .middleware import put_note
from .middleware import put_loan
from .middleware import get_book
from .middleware import get_user
from .middleware import get_note
from .middleware import get_loan
from .middleware import add_books
from .middleware import add_users
from .middleware import add_notes
from .middleware import add_loans


def init_api_routes(app):
    if app:
        api = Api(app)

        book_api = api.namespace('books', description='Operations on books')
        user_api = api.namespace('users', description='Operations on users')
        loan_api = api.namespace('loans', description='Operations on loans')
        list_api = api.namespace('lists', description='Operations on' +
                                 ' book lists')
        note_api = api.namespace('notes', description='Operations on' +
                                 ' book notes')

        add_book = api.model('Book', {
                'name': fields.String,
                'author': fields.String,
                'subject': fields.String,
                'status': fields.String,
                'published_date': fields.DateTime
                })

        search_book = api.model('Search_Book', {
                'author': fields.String,
                'subject': fields.String,
                'published_date_from': fields.DateTime,
                'published_date_to': fields.DateTime
                })

        add_user = api.model('User', {
                'name': fields.String,
                'email': fields.String,
                'phone': fields.String,
                'birth_year': fields.Integer
                })

        add_loan = api.model('Loan', {
                'book_id': fields.Integer,
                'user_id': fields.Integer,
                'status': fields.String,
                'borrowed_date': fields.DateTime,
                'return_date': fields.DateTime
                })

        add_list = api.model('List', {
                'user_id': fields.Integer,
                'book_ids': fields.Integer,
                'list_name': fields.String
                })

        add_note = api.model('Note', {
                'book_id': fields.Integer,
                'user_id': fields.Integer,
                'notes': fields.String
                })

        @book_api.route('/<int:book_id>')
        class GetBooks(Resource):
                @book_api.response(200, 'Success')
                @book_api.response(404, 'Not Found')
                @book_api.doc(params={'book_id': 'The book_id of the ' +
                                      'book to be retrieved'})
                def get(self, book_id):
                        '''Shows the details of a book'''
                        return get_book(book_id).serialize(), 200

                @book_api.response(200, 'Success')
                @book_api.response(400, 'Validation Error')
                @book_api.doc(params={'book_id': 'The book_id of the ' +
                                      'book to be updated'})
                @book_api.expect(add_book)
                def put(self, book_id):
                        '''Updates a book'''
                        data = request.json
                        book = get_book(book_id)
                        if 'name' in data:
                                book.name = data['name']
                        if 'author' in data:
                                book.author = data['author']
                        if 'subject' in data:
                                book.subject = data['subject']
                        if 'status' in data:
                                book.status = data['status']
                        if 'published_date' in data:
                                book.published_date = data['published_date']

                        return put_book(book).serialize(), 200

                @book_api.response(204, 'No Content')
                @book_api.response(404, 'Not Found')
                @book_api.doc(params={'book_id': 'The book_id of the ' +
                                      'book to be deleted'})
                def delete(self, book_id):
                        '''Deletes the book'''
                        get_book(book_id)
                        return delete_book(book_id), 204

        @book_api.route('')
        class AddBooks(Resource):
                @book_api.response(201, 'Created')
                @book_api.response(400, 'Validation Error')
                @book_api.expect(add_book)
                def post(self):
                        '''Creates a book'''
                        data = request.json
                        if 'name' in data:
                                name = data['name']
                        if 'author' in data:
                                author = data['author']
                        if 'subject' in data:
                                subject = data['subject']
                        if 'status' in data:
                                status = data['status']
                        if 'published_date' in data:
                                published_date = data['published_date']

                        book = Library(name=name, author=author,
                                       subject=subject, status=status,
                                       published_date=published_date)
                        return add_books(book).serialize(), 201

                @book_api.response(200, 'Success')
                @book_api.response(201, 'No Content')
                def get(self):
                        '''Shows a list of all books'''
                        return get_books(), 200

        @book_api.route('/search')
        class SearchBooks(Resource):
                @book_api.response(200, 'Success')
                @book_api.response(201, 'No Content')
                @book_api.response(400, 'Validation Error')
                @book_api.expect(search_book)
                def post(self):
                        '''Searches for a book'''
                        data = request.json
                        if 'author' in data:
                                author = data['author']
                        else:
                                author = None
                        if 'subject' in data:
                                subject = data['subject']
                        else:
                                subject = None
                        if 'published_date_from' in data:
                                published_date_from = data['published_date_from']
                        else:
                                published_date_from = None
                        if 'published_date_to' in data:
                                published_date_to = data['published_date_to']
                        else:
                                published_date_to = None
                        return search_books(author, subject, published_date_from, published_date_to), 200

        @user_api.route('/<int:user_id>')
        class GetUsers(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be retrieved'})
                def get(self, user_id):
                        '''Shows details of a user'''
                        return get_user(user_id).serialize(), 200

                @user_api.response(200, 'Success')
                @user_api.response(400, 'Validation Error')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be updated'})
                @user_api.expect(add_user)
                def put(self, user_id):
                        '''Updates details of a user'''
                        data = request.json
                        user = get_user(user_id)
                        if 'name' in data:
                                user.name = data['name']
                        if 'email' in data:
                                user.email = data['email']
                        if 'phone' in data:
                                user.phone = data['phone']
                        if 'birth_year' in data:
                                user.birth_year = data['birth_year']
                        return put_user(user).serialize(), 200

                @user_api.response(204, 'No Content')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be deleted'})
                def delete(self, user_id):
                        '''Deletes a user'''
                        get_user(user_id)
                        return delete_user(user_id), 204

        @user_api.route('')
        class AddUsers(Resource):
                @user_api.response(201, 'Created')
                @user_api.response(400, 'Validation Error')
                @user_api.expect(add_user)
                def post(self):
                        '''Creates a user'''
                        data = request.json
                        if 'name' in data:
                                name = data['name']
                        if 'email' in data:
                                email = data['email']
                        if 'phone' in data:
                                phone = data['phone']
                        if 'birth_year' in data:
                                birth_year = data['birth_year']

                        user = User(name=name, email=email,
                                    phone=phone, birth_year=birth_year)
                        return add_users(user).serialize(), 201

        @note_api.route('/<int:note_id>')
        class GetNotes(Resource):
                @note_api.response(200, 'Success')
                @note_api.response(404, 'Not Found')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note'})
                def get(self, note_id):
                        '''Shows details of a note'''
                        return get_note(note_id).serialize(), 200

                @note_api.response(200, 'Success')
                @note_api.response(400, 'Validation Error')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note to be updated'})
                @note_api.expect(add_note)
                def put(self, note_id):
                        '''Updates details of a note'''
                        data = request.json
                        note = get_note(note_id)
                        if 'book_id' in data:
                                note.book_id = data['book_id']
                                get_book(note.book_id)
                        if 'user_id' in data:
                                note.user_id = data['user_id']
                                get_user(note.user_id)
                        if 'notes' in data:
                                note.notes = data['notes']
                        return put_note(note).serialize(), 200

                @note_api.response(204, 'No Content')
                @note_api.response(404, 'Not Found')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note to be deleted'})
                def delete(self, note_id):
                        '''Deletes a note'''
                        get_note(note_id)
                        return delete_note(note_id), 204

        @note_api.route('')
        class AddNotes(Resource):
                @note_api.response(201, 'Created')
                @note_api.response(400, 'Validation Error')
                @note_api.expect(add_note)
                def post(self):
                        '''Creates a note'''
                        data = request.json
                        if 'book_id' in data:
                                book_id = data['book_id']
                                get_book(book_id)
                        if 'user_id' in data:
                                user_id = data['user_id']
                                get_user(user_id)
                        if 'notes' in data:
                                notes = data['notes']

                        note = Notes(book_id=book_id, user_id=user_id,
                                     notes=notes)
                        return add_notes(note).serialize(), 201

        @user_api.route('/<int:user_id>/books/<int:book_id>/notes')
        class AddNotes(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.param('user_id', 'The user_id of the user')
                @user_api.param('book_id', 'The book_id of the book')
                def get(self, user_id, book_id):
                        '''Get details of a note using user_id and book_id'''
                        return find_note(user_id, book_id).serialize(), 200

        @loan_api.route('')
        class AllLoans(Resource):
                @loan_api.response(200, 'Success')
                @loan_api.response(404, 'Not Found')
                def get(self):
                        '''Shows details of all loans'''
                        return get_loans(), 200

        @user_api.route('/<int:user_id>/loans')
        class AddLoans(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'loans to be retrieved for'})
                def get(self, user_id):
                        '''Shows details of all loans of the user'''
                        get_user(user_id)
                        return get_userloans(user_id), 200

                @user_api.response(201, 'Created')
                @user_api.response(400, 'Validation Error')
                @user_api.expect(add_loan)
                def post(self, user_id):
                        '''Creates a loan'''
                        data = request.json
                        if 'book_id' in data:
                                book_id = data['book_id']
                                get_book(book_id)
                        if 'user_id' in data:
                                user_id = data['user_id']
                                get_user(user_id)
                        if 'status' in data:
                                status = data['status']
                        if 'borrowed_date' in data:
                                borrowed_date = data['borrowed_date']
                        if 'return_date' in data:
                                return_date = data['return_date']

                        loan = Loan(book_id=book_id, user_id=user_id,
                                    status=status, borrowed_date=borrowed_date,
                                    return_date=return_date)
                        return add_loans(loan).serialize(), 201

        @loan_api.route('/<int:loan_id>')
        class GetLoans(Resource):
                @loan_api.response(200, 'Success')
                @loan_api.response(400, 'Validation Error')
                @loan_api.doc(params={'loan_id': 'The loan_id of the ' +
                                      'loan to be updated'})
                @loan_api.expect(add_loan)
                def put(self, loan_id):
                        '''Updates a loan'''
                        data = request.json
                        loan = get_loan(loan_id)
                        if 'book_id' in data:
                                loan.book_id = data['book_id']
                                get_book(loan.book_id)
                        if 'user_id' in data:
                                loan.user_id = data['user_id']
                                get_user(loan.user_id)
                        if 'status' in data:
                                loan.status = data['status']
                        if 'borrowed_date' in data:
                                loan.borrowed_date = data['borrowed_date']
                        if 'return_date' in data:
                                loan.return_date = data['return_date']
                        return put_loan(loan).serialize(), 200

                @loan_api.response(204, 'No Content')
                @loan_api.response(404, 'Not Found')
                @loan_api.doc(params={'loan_id': 'The loan_id of the ' +
                                      'loan to be deleted'})
                def delete(self, loan_id):
                        '''Deletes a loan'''
                        get_loan(loan_id)
                        return delete_loan(loan_id), 204

                @loan_api.response(200, 'Success')
                @loan_api.response(404, 'Not Found')
                @loan_api.doc(params={'loan_id': 'The loan_id of the ' +
                                      'loan to be retrieved'})
                def get(self, loan_id):
                        '''Shows details of the loan'''
                        return get_loan(loan_id).serialize(), 200

        @user_api.route('/<int:user_id>/lists')
        class AddLists(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'lists to be retrieved for'})
                def get(self, user_id):
                        '''Shows all lists of a user'''
                        return [user_id], 200

                @user_api.response(201, 'Created')
                @user_api.response(400, 'Validation Error')
                @user_api.expect(add_list)
                def post(self):
                        '''Creates a list'''
                        return {"message": "List Created Successfully"}, 201

        @list_api.route('/<int:list_id>')
        class GetLists(Resource):
                @list_api.response(200, 'Success')
                @list_api.response(404, 'Not Found')
                @list_api.doc(params={'list_id': 'The list_id of the ' +
                                      'list to be retrieved for'})
                def get(self, list_id):
                        '''Shows details of a list'''
                        return [list_id], 200

                @list_api.response(200, 'Success')
                @list_api.response(400, 'Validation Error')
                @list_api.doc(params={'list_id': 'The list_id of the ' +
                                      'list to be updated'})
                @list_api.expect(add_loan)
                def put(self, list_id):
                        '''Updates a list'''
                        return {"message": "List Updated Successfully"}, 200

                @list_api.response(204, 'No Content')
                @list_api.response(404, 'Not Found')
                @list_api.doc(params={'list_id': 'The list_id of the ' +
                                      'list to be deleted'})
                def delete(self, list_id):
                        '''Deletes a list'''
                        return {"message": "List Deleted Successfully"}, 204
