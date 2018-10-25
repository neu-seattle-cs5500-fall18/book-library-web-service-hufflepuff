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
        :return: The books.
        """
        all_books = self.session.query(Library).all()
        book_list = [book.serialize() for book in all_books]
        return book_list

    def put_book(self, book):
        """
        :return: The books.
        """
        self.session.add(book)
        self.session.commit()
        the_book = self.session.query(Library).filter_by(book_id=book.book_id).first()
        return the_book

    def get_book(self, book_id):
        """
        :return: The books.
        """
        the_book = self.session.query(Library).filter_by(book_id=book_id).first()
        return the_book

    def search_books(self, author, subject, published_date_from, published_date_to):
        """
        :return: The books matching the search crieteria.
        """
        query = self.session.query(Library)
        if author:
            query = query.filter_by(author=author)
        if subject:
            query = query.filter_by(subject=subject)
        if published_date_from:
            query = query.filter(Library.published_date >= published_date_from)
        if published_date_to:
            query = query.filter(Library.published_date <= published_date_to)

        all_books = query.all()
        print(all_books)
        book_list = [book.serialize() for book in all_books]
        return book_list

    def delete_book(self, book_id):
        """
        :return: The books.
        """
        the_book = self.session.query(Library).filter_by(book_id=book_id).first()
        self.session.delete(the_book)
        self.session.commit()
        return "Deleted the book"

    def get_users(self):
        """
        :return: The users.
        """
        all_users = []
        all_users = self.session.query(User).all()
        return [user.serialize() for user in all_users]

    def add_book(self, book):
        """
        :return: The book added with book_id.
        """
        self.session.add(book)
        self.session.commit()
        the_book = self.session.query(Library).filter_by(name=book.name,
                                                         author=book.author,
                                                         subject=book.subject,
                                                         status=book.status).first()
        return the_book

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
