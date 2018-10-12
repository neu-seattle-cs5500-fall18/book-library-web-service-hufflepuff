from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model
import json

#
# to use jsonld, we should install pyLD using:
#        pip install PyLD
#
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
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "birth_year": self.birth_year
        }, self.get_context())
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "user_id": "user_id",
                "name": "name",
                "email": "email",
                "phone": "phone",
                "birth_year": "birth_year"
            }
        }
