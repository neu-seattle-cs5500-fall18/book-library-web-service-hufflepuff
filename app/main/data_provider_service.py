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

    def get_loans(self):
        """
        :return: The loans.
        """
        all_loans = self.session.query(Loan).all()
        loan_list = [loan.serialize() for loan in all_loans]
        return loan_list

    def get_userloans(self, user_id):
        """
        :return: The loans.
        """
        all_loans = self.session.query(Loan).filter_by(user_id=user_id).all()
        loan_list = [loan.serialize() for loan in all_loans]
        return loan_list

    def put_book(self, book):
        """
        :return: The books.
        """
        self.session.add(book)
        self.session.commit()
        the_book = self.session.query(Library).filter_by(book_id=book.book_id).first()
        return the_book

    def put_user(self, user):
        """
        :return: The updated user.
        """
        self.session.add(user)
        self.session.commit()
        the_user = self.session.query(User).filter_by(user_id=user.user_id).first()
        return the_user

    def put_note(self, note):
        """
        :return: The updated note.
        """
        self.session.add(note)
        self.session.commit()
        the_note = self.session.query(Notes).filter_by(note_id=note.note_id).first()
        return the_note

    def put_loan(self, loan):
        """
        :return: The updated loan.
        """
        self.session.add(loan)
        self.session.commit()
        book = self.get_book(loan.book_id)
        book.status = loan.status
        self.put_book(book)
        the_loan = self.session.query(Loan).filter_by(loan_id=loan.loan_id).first()
        return the_loan

    def get_book(self, book_id):
        """
        :return: The books.
        """
        the_book = self.session.query(Library).filter_by(book_id=book_id).first()
        return the_book

    def get_user(self, user_id):
        """
        :return: The user.
        """
        the_user = self.session.query(User).filter_by(user_id=user_id).first()
        return the_user

    def get_note(self, note_id):
        """
        :return: The notes.
        """
        the_note = self.session.query(Notes).filter_by(note_id=note_id).first()
        return the_note

    def get_loan(self, loan_id):
        """
        :return: The loan.
        """
        the_loan = self.session.query(Loan).filter_by(loan_id=loan_id).first()
        return the_loan

    def find_note(self, user_id, book_id):
        """
        :return: The notes.
        """
        the_note = self.session.query(Notes).filter_by(user_id=user_id,
                                                       book_id=book_id).first()
        return the_note

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

    def delete_user(self, user_id):
        """
        :return: The user to be deleted.
        """
        the_user = self.session.query(User).filter_by(user_id=user_id).first()
        self.session.delete(the_user)
        self.session.commit()
        return "Deleted the user"

    def delete_note(self, note_id):
        """
        :return: The note to be deleted.
        """
        the_note = self.session.query(Notes).filter_by(note_id=note_id).first()
        self.session.delete(the_note)
        self.session.commit()
        return "Deleted the notes"

    def delete_loan(self, loan_id):
        """
        :return: The loan to be deleted.
        """
        the_loan = self.session.query(Loan).filter_by(loan_id=loan_id).first()
        self.session.delete(the_loan)
        self.session.commit()
        book = self.get_book(the_loan.book_id)
        book.status = "Available"
        self.put_book(book)
        return "Deleted the loan"

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

    def add_user(self, user):
        """
        :return: The user added with user_id.
        """
        self.session.add(user)
        self.session.commit()
        the_user = self.session.query(Library).filter_by(name=user.name,
                                                         email=user.email,
                                                         phone=user.phone,
                                                         birth_year=user.birth_year).first()
        return the_user

    def add_note(self, note):
        """
        :return: The note added with note_id.
        """
        self.session.add(note)
        self.session.commit()
        the_note = self.session.query(Notes).filter_by(book_id=note.book_id,
                                                       user_id=note.user_id,
                                                       notes=note.notes).first()
        return the_note

    def add_loan(self, loan):
        """
        :return: The loan added with loan_id.
        """
        self.session.add(loan)
        self.session.commit()
        book = self.get_book(loan.book_id)
        book.status = loan.status
        self.put_book(book)
        the_loan = self.session.query(Loan).filter_by(book_id=loan.book_id,
                                                      user_id=loan.user_id,
                                                      status=loan.status).first()
        return the_loan
