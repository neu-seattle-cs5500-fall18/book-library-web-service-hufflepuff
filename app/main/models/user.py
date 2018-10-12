from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class User(Model):
    """
        The user model for storing user details
    """
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(25), unique=True)
    phone = Column(String(20), unique=True)
    birth_year = Column(Integer)

    def __init__(self, user_id, name, email, phone, birth_year):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.birth_year = birth_year

    def __repr__(self):
        return '<userid {}>'.format(self.user_id)

    #
    # METHODS
    #

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/user_id": self.user_id,
            "http://schema.org/name": self.name,
            "http://schema.org/email": self.email,
            "http://schema.org/phone": self.phone,
            "http://schema.org/birth_year": self.birth_year
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "user_id": "http://schema.org/user_id",
                "name": "http://schema.org/name",
                "email": "http://schema.org/email",
                "phone": "http://schema.org/phone",
                "birth_year": "http://schema.org/birth_year"
            }
        }
