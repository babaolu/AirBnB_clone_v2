#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    def __init__(self, *args, **kwargs):
        """ Setting up initialization for the User class
            *args: Is not been used
        """
        super().__init__(**kwargs)
        class_attr = ["email", "password", "first_name", "last_name"]
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if kwargs:
            for k in class_attr:
                val = kwargs.get(k)
                if val:
                    setattr(self, k, val)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship('Place', backref='user',
                              cascade='all, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
