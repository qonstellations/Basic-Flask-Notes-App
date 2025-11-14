from datetime import datetime
from flask_login import UserMixin
from bson.objectid import ObjectId
from . import db

class User(UserMixin):
    def __init__(self, _id : ObjectId | None, email : str, password : str, first_name : str):
        self._id = _id
        self.email = email
        self.password = password
        self.first_name = first_name

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id = doc["_id"],
            email = doc["email"],
            password = doc["password"],
            first_name = doc["first_name"],
        )

    def get_id(self):
        return self._id

    def conv_to_dict(self):
        base = {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
        }
        
        if self._id is not None:
            base["_id"] = self._id

        return base


class Note:
    def __init__(self, _id: ObjectId | None, user_id: str, date: datetime, data: str):
        self._id = _id
        self.user_id = user_id
        self.date = date
        self.data = data

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id = doc["_id"],
            user_id = doc["user_id"],
            date = doc["date"],
            data = doc["data"]
        )

    def conv_to_dict(self):
        base = {
            "user_id": self.user_id,
            "date": self.date,
            "data": self.data
        }
        if self._id is not None:
            base["_id"] = self._id
        return base