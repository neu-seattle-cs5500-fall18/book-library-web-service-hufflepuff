from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import json
from flask_mail import Message, Mail
from smtplib import SMTP

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
        self.app = None
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_app(self, app):
        """
        Initializes the app
        :return: None
        """
        self.app = app

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
        loan_list = []
        for loan in all_loans:
            user = self.get_user(loan.user_id).serialize()
            loan_data = loan.serialize()
            del loan_data['user_id']
            loan_data['user'] = user
            loan_list += [loan_data]
        return loan_list

    def get_userloans(self, user_id):
        """
        :return: The loans.
        """
        all_loans = self.session.query(Loan).filter_by(user_id=user_id).all()
        loan_list = [loan.serialize() for loan in all_loans]
        return loan_list

    def get_userlists(self, user_id):
        """
        :return: The lists of a user.
        """
        all_lists = self.session.query(List).filter_by(user_id=user_id).all()
        user_list = []
        for each in all_lists:
            list_items = self.session.query(Listitem).filter_by(list_id=each.list_id).all()
            items = [self.get_book(item.book_id).serialize() for item in list_items]
            add_list = each.serialize()
            add_list['books'] = items
            user_list += [add_list]
        return user_list

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

    def remind_user(self, user, book, return_by):
        """
        :return: The updated user.
        """
        the_loan = self.session.query(Loan).filter_by(user_id=user.user_id,
                                                      book_id=book.book_id,
                                                      status="loaned out").first()
        the_loan.return_by = return_by
        self.session.add(the_loan)
        self.session.commit()
        line1 = f'Hello, {user.name}!\nThe library wants you to return the book '
        line2 = f'"{book.name}" by the date {return_by}. This is just a friendly reminder for the same.'
        email_body = line1 + line2
        email_content = "Return Book Reminder"
        mail = Mail()
        mail.init_app(self.app)
        msg = Message(email_content,
                      recipients=["krishnakaranam3732@gmail.com"],
                      sender="bookscatalogproject@gmail.com",
                      body=email_body)
        mail.send(msg)
        return the_loan

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
        if loan.status.lower() == "returned":
            book.status = "Available"
        else:
            book.status = loan.status
        self.put_book(book)
        the_loan = self.session.query(Loan).filter_by(loan_id=loan.loan_id).first()
        return the_loan

    def put_list(self, the_list, books):
        """
        :return: The updated loan.
        """
        the_items = self.session.query(Listitem).filter_by(list_id=the_list.list_id).all()
        for each in the_items:
            if each.book_id not in books:
                self.session.delete(each)
            else:
                books.remove(each.book_id)

        for book_id in books:
            listitem = Listitem(the_list.list_id, book_id)
            self.session.add(listitem)

        self.session.add(the_list)
        self.session.commit()
        return the_list

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

    def get_list(self, list_id):
        """
        :return: The list.
        """
        the_list = self.session.query(List).filter_by(list_id=list_id).first()
        list_items = self.session.query(Listitem).filter_by(list_id=list_id).all()
        items = [self.get_book(item.book_id).serialize() for item in list_items]
        if the_list:
            add_list = the_list.serialize()
        else:
            return None
        add_list['books'] = items
        return add_list

    def get_list_object(self, list_id):
        """
        :return: The list object.
        """
        the_list = self.session.query(List).filter_by(list_id=list_id).first()
        return the_list

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

    def delete_list(self, list_id):
        """
        :return: The list to be deleted.
        """
        the_items = self.session.query(Listitem).filter_by(list_id=list_id).all()
        for each in the_items:
            self.session.delete(each)
        the_list = self.session.query(List).filter_by(list_id=list_id).first()
        self.session.delete(the_list)
        self.session.commit()
        return "Deleted the list"

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

    def add_list(self, add_list, book_ids):
        """
        :return: The loan added with loan_id.
        """
        the_list = self.session.query(List).filter_by(user_id=add_list.user_id,
                                                      list_name=add_list.list_name).first()
        if not the_list:
            self.session.add(add_list)
            self.session.commit()
        the_list = self.session.query(List).filter_by(user_id=add_list.user_id,
                                                      list_name=add_list.list_name).first()
        for book_id in book_ids:
            listitem = Listitem(the_list.list_id, book_id)
            the_item = self.session.query(Listitem).filter_by(list_id=the_list.list_id,
                                                              book_id=book_id).first()
            if not the_item:
                self.session.add(listitem)
        self.session.commit()
        return the_list
