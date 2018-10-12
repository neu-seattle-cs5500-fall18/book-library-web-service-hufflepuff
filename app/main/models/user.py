from sqlalchemy import Column, String, Integer, Date, ForeignKey


class user(Model):
    """
        The user model for storing user details
    """
    __tablename__ = 'user'

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
