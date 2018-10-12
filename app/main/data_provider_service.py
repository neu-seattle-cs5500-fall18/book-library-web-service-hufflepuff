from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import User
from .models import Library
from .models import Notes
from .models import Loan
from .models import init_database


class DataProviderService:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """
        if not engine:
            raise ValueError('Values not supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

    def get_users(self):
        """
        :return: The users.
        """
        all_users = []
        all_users = self.session.query(User).order_by(User.name).all()
        return all_users
