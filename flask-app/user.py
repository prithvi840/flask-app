from flask import session
from common import Database, Utils
import uuid


class User:
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one(collection='users', query={"email": email})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is not None:
            return f"{email} already exists"
        if not Utils.email_is_valid(email):
            raise ValueError("Format of email is incorrect")

        new_user = cls(email, password)
        new_user.save_to_mongo()
        return True

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert(collection="users", data=self.json())
