#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    def __init__(self, *args, **kwargs):
        """ Setting up initialization for the Review class
            *args: Is not been used
        """
        super().__init__(**kwargs)
        class_attr = ["text", "place_id", "user_id"]
        self.text = ""
        self.place_id = ""
        self.user_id = ""
        if kwargs:
             for k in class_attr:
                val = kwargs.get(k)
                if val:
                    setattr(self, k, val)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
