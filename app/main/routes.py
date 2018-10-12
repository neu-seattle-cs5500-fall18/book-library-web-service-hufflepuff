from .middleware import initialize_database as init_db
from .middleware import get_users


def init_api_routes(app):
    if app:
        app.add_url_rule('/api/users',
                         'get_users', get_users, methods=['GET'])
