from .middleware import initialize_database as init_db
from flask_restplus import Api, Resource, fields
from .middleware import get_books
from .middleware import get_user
from .middleware import get_users
from .middleware import add_books
from .middleware import add_users


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
                        return [book_id], 200

                @book_api.response(200, 'Success')
                @book_api.response(400, 'Validation Error')
                @book_api.doc(params={'book_id': 'The book_id of the ' +
                                      'book to be updated'})
                @book_api.expect(add_book)
                def put(self, book_id):
                        '''Updates a book'''
                        return {"message": "Book Updated Successfully"}, 200

                @book_api.response(204, 'No Content')
                @book_api.response(404, 'Not Found')
                @book_api.doc(params={'book_id': 'The book_id of the ' +
                                      'book to be deleted'})
                def delete(self, book_id):
                        '''Deletes the book'''
                        return {"message": "Book Deleted Successfully"}, 204

        @book_api.route('')
        class AddBooks(Resource):
                @book_api.response(201, 'Created')
                @book_api.response(400, 'Validation Error')
                @book_api.expect(add_book)
                def post(self):
                        '''Creates a book'''
                        return {"message": "Book Added Successfully"}, 201

                @book_api.response(200, 'Success')
                @book_api.response(201, 'No Content')
                def get(self):
                        '''Shows a list of all books'''
                        return ["all books"], 200

        @book_api.route('/search')
        class SearchBooks(Resource):
                @book_api.response(200, 'Success')
                @book_api.response(201, 'No Content')
                @book_api.response(400, 'Validation Error')
                @book_api.expect(search_book)
                def post(self):
                        '''Searches for a book'''
                        return {"message": "Matching books"}, 200

        @user_api.route('/<int:user_id>')
        class GetUsers(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be retrieved'})
                def get(self, user_id):
                        '''Shows details of a user'''
                        return [user_id], 200

                @user_api.response(200, 'Success')
                @user_api.response(400, 'Validation Error')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be updated'})
                @user_api.expect(add_user)
                def put(self, user_id):
                        '''Updates details of a user'''
                        return {"message": "User Updated Successfully"}, 200

                @user_api.response(204, 'No Content')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user to be deleted'})
                def delete(self, user_id):
                        '''Deletes a user'''
                        return {"message": "User Deleted Successfully"}, 204

        @user_api.route('')
        class AddUsers(Resource):
                @user_api.response(201, 'Created')
                @user_api.response(400, 'Validation Error')
                @user_api.expect(add_user)
                def post(self):
                        '''Creates a user'''
                        return {"message": "User Created Successfully"}, 201

        @note_api.route('/<int:note_id>')
        class GetNotes(Resource):
                @note_api.response(200, 'Success')
                @note_api.response(404, 'Not Found')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note'})
                def get(self, note_id):
                        '''Shows details of a note'''
                        return {"note": str(note_id)}, 200

                @note_api.response(200, 'Success')
                @note_api.response(400, 'Validation Error')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note to be updated'})
                @note_api.expect(add_user)
                def put(self, note_id):
                        '''Updates details of a note'''
                        return {"message": "Notes Updated Successfully"}, 200

                @note_api.response(204, 'No Content')
                @note_api.response(404, 'Not Found')
                @note_api.doc(params={'note_id': 'The note_id of the ' +
                                      'note to be deleted'})
                def delete(self, note_id):
                        '''Deletes a note'''
                        return {"message": "Notes Deleted Successfully"}, 204

        @note_api.route('')
        class AddNotes(Resource):
                @note_api.response(201, 'Created')
                @note_api.response(400, 'Validation Error')
                @note_api.expect(add_note)
                def post(self):
                        '''Creates a note'''
                        return {"message": "Notes Created Successfully"}, 201

        @user_api.route('/<int:user_id>/books/<int:book_id>/notes')
        class AddNotes(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'user'},
                                     {'book_id': 'The book_id of the ' +
                                      'book'})
                def get(self, user_id, book_id):
                        '''Get details of a note using user_id and book_id'''
                        return {"note": str(user_id) + " " + str(book_id)}, 200

        @loan_api.route('')
        class AllLoans(Resource):
                @loan_api.response(200, 'Success')
                @loan_api.response(404, 'Not Found')
                def get(self):
                        '''Shows details of all loans'''
                        return ["All Loans"], 200

        @user_api.route('/<int:user_id>/loans')
        class AddLoans(Resource):
                @user_api.response(200, 'Success')
                @user_api.response(404, 'Not Found')
                @user_api.doc(params={'user_id': 'The user_id of the ' +
                                      'loans to be retrieved for'})
                def get(self, user_id):
                        '''Shows details of all loans of the user'''
                        return [user_id], 200

                @user_api.response(201, 'Created')
                @user_api.response(400, 'Validation Error')
                @user_api.expect(add_loan)
                def post(self):
                        '''Creates a loan'''
                        return {"message": "User Created Successfully"}, 201

        @loan_api.route('/<int:loan_id>')
        class GetLoans(Resource):
                @loan_api.response(200, 'Success')
                @loan_api.response(400, 'Validation Error')
                @loan_api.doc(params={'loan_id': 'The loan_id of the ' +
                                      'loan to be updated'})
                @loan_api.expect(add_loan)
                def put(self, loan_id):
                        '''Updates a loan'''
                        return {"message": "Loan Updated Successfully"}, 200

                @loan_api.response(204, 'No Content')
                @loan_api.response(404, 'Not Found')
                @loan_api.doc(params={'loan_id': 'The loan_id of the ' +
                                      'loan to be deleted'})
                def delete(self, loan_id):
                        '''Deletes a loan'''
                        return {"message": "Loan Deleted Successfully"}, 204

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
