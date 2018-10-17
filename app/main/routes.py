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

        book_api = api.namespace('book', description='Operations on books')
        user_api = api.namespace('user', description='Operations on users')
        loan_api = api.namespace('loan', description='Operations on loans')
        list_api = api.namespace('list', description='Operations on' +
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

        @book_api.route('/api/books/<int:book_id>')
        class GetBooks(Resource):
                @api.response(200, 'Success')
                @api.response(404, 'Not Found')
                @api.doc(params={'book_id': 'The book_id of the ' +
                                 'book to be retrieved'})
                def get(self, book_id):
                        return [book_id], 200

                @api.response(200, 'Success')
                @api.response(400, 'Validation Error')
                @api.doc(params={'book_id': 'The book_id of the ' +
                                 'book to be updated'})
                @api.expect(add_book)
                def put(self, book_id):
                        return {"message": "Book Updated Successfully"}, 200

                @api.response(204, 'No Content')
                @api.response(404, 'Not Found')
                @api.doc(params={'book_id': 'The book_id of the ' +
                                 'book to be deleted'})
                def delete(self, book_id):
                        return {"message": "Book Deleted Successfully"}, 204

        @book_api.route('/api/books')
        class AddBooks(Resource):
                @api.response(201, 'Created')
                @api.response(400, 'Validation Error')
                @api.expect(add_book)
                def post(self):
                        return {"message": "Book Added Successfully"}, 201

        @user_api.route('/api/users/<int:user_id>')
        class GetUsers(Resource):
                @api.response(200, 'Success')
                @api.response(404, 'Not Found')
                @api.doc(params={'user_id': 'The user_id of the ' +
                                 'user to be retrieved'})
                def get(self, user_id):
                        return [user_id], 200

                @api.response(200, 'Success')
                @api.response(400, 'Validation Error')
                @api.doc(params={'user_id': 'The user_id of the ' +
                                 'user to be updated'})
                @api.expect(add_user)
                def put(self, user_id):
                        return {"message": "User Updated Successfully"}, 200

                @api.response(204, 'No Content')
                @api.response(404, 'Not Found')
                @api.doc(params={'user_id': 'The user_id of the ' +
                                 'user to be deleted'})
                def delete(self, user_id):
                        return {"message": "User Deleted Successfully"}, 204

        @user_api.route('/api/users')
        class AddUsers(Resource):
                @api.response(201, 'Created')
                @api.response(400, 'Validation Error')
                @api.expect(add_user)
                def post(self):
                        return {"message": "User Created Successfully"}, 201

        @note_api.route('/api/notes/<int:note_id>')
        class GetNotes(Resource):
                @api.response(200, 'Success')
                @api.response(404, 'Not Found')
                @api.doc(params={'note_id': 'The note_id of the ' +
                                 'note'})
                def get(self, note_id):
                        return {"note": str(note_id)}, 200

                @api.response(200, 'Success')
                @api.response(400, 'Validation Error')
                @api.doc(params={'note_id': 'The note_id of the ' +
                                 'note to be updated'})
                @api.expect(add_user)
                def put(self, note_id):
                        return {"message": "Notes Updated Successfully"}, 200

                @api.response(204, 'No Content')
                @api.response(404, 'Not Found')
                @api.doc(params={'note_id': 'The note_id of the ' +
                                 'note to be deleted'})
                def delete(self, note_id):
                        return {"message": "Notes Deleted Successfully"}, 204

        @note_api.route('/api/notes')
        class AddNotes(Resource):
                @api.response(201, 'Created')
                @api.response(400, 'Validation Error')
                @api.expect(add_note)
                def post(self):
                        return {"message": "Notes Created Successfully"}, 201

        @loan_api.route('/api/users/<int:user_id>/loans')
        class AddLoans(Resource):
                @api.response(200, 'Success')
                @api.response(404, 'Not Found')
                @api.doc(params={'user_id': 'The user_id of the ' +
                                 'loans to be retrieved for'})
                def get(self, user_id):
                        return [user_id], 200

                @api.response(201, 'Created')
                @api.response(400, 'Validation Error')
                @api.expect(add_loan)
                def post(self):
                        return {"message": "User Created Successfully"}, 201

        @loan_api.route('/api/loans/<int:loan_id>')
        class GetLoans(Resource):
                @api.response(200, 'Success')
                @api.response(400, 'Validation Error')
                @api.doc(params={'loan_id': 'The loan_id of the ' +
                                 'loan to be updated'})
                @api.expect(add_loan)
                def put(self, loan_id):
                        return {"message": "Loan Updated Successfully"}, 200

                @api.response(204, 'No Content')
                @api.response(404, 'Not Found')
                @api.doc(params={'loan_id': 'The loan_id of the ' +
                                 'loan to be deleted'})
                def delete(self, loan_id):
                        return {"message": "Loan Deleted Successfully"}, 204

        @list_api.route('/api/users/<int:user_id>/lists')
        class AddLists(Resource):
                @api.response(200, 'Success')
                @api.response(404, 'Not Found')
                @api.doc(params={'user_id': 'The user_id of the ' +
                                 'lists to be retrieved for'})
                def get(self, user_id):
                        return [user_id], 200

                @api.response(201, 'Created')
                @api.response(400, 'Validation Error')
                @api.expect(add_list)
                def post(self):
                        return {"message": "List Created Successfully"}, 201

        @list_api.route('/api/lists/<int:list_id>')
        class GetLists(Resource):
                @api.response(200, 'Success')
                @api.response(400, 'Validation Error')
                @api.doc(params={'list_id': 'The list_id of the ' +
                                 'list to be updated'})
                @api.expect(add_loan)
                def put(self, list_id):
                        return {"message": "List Updated Successfully"}, 200

                @api.response(204, 'No Content')
                @api.response(404, 'Not Found')
                @api.doc(params={'list_id': 'The list_id of the ' +
                                 'list to be deleted'})
                def delete(self, list_id):
                        return {"message": "List Deleted Successfully"}, 204
