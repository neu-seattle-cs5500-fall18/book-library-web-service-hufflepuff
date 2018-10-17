from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import json

from .models.user import User
from .models.library import Library
from .models.notes import Notes
from .models.loan import Loan
from .models.list import List
from .models.listitem import Listitem
from .models.init_database import init_database


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

    def get_books(self):
        """
        :return: The users.
        """
        all_books = []
        all_books = self.session.query(Library).all()
        return [book.serialize() for book in all_books]

    def get_users(self):
        """
        :return: The users.
        """
        all_users = []
        all_users = self.session.query(User).all()
        return [user.serialize() for user in all_users]

    def add_books(self, name, author, subject,
                  status, published_date):
        """
        :return: The book added with book_id.
        """
        new_book = Library(name=name,
                           author=author,
                           subject=subject,
                           status=status,
                           published_date=published_date)

        self.session.add(new_book)
        self.session.commit()

        return new_book.book_id

    def add_users(self, name, email, phone,
                  birth_year):
        """
        :return: The user added with user_id.
        """
        new_user = User(name=name,
                        email=email,
                        phone=phone,
                        birth_year=birth_year)

        self.session.add(new_user)
        self.session.commit()

        return new_user.user_id
