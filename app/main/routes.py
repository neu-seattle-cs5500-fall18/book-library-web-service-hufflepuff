from .middleware import initialize_database as init_db
from .middleware import get_users


def init_api_routes(app):
    if app:
        app.add_url_rule('/api/users',
                         'get_users', get_users, methods=['GET'])
        # app.add_url_rule('/api/books',
        #                  'get_books', get_books, methods=['GET'])
        app.add_url_rule('/api/books',
                         'add_books', add_books, methods=['POST'])
        # app.add_url_rule('/api/books',
        #                  'update_books', update_books, methods=['PUT'])
        # app.add_url_rule('/api/books',
        #                  'remove_books', remove_books, methods=['DELETE'])
