#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    def __init__(self, *args, **kwargs):
        """ Setting up initialization for the City class
            *args: Is not been used
        """
        super().__init__(**kwargs)
        class_attr = ["name", "state_id"]
        self.name = ""
        self.state_id = ""
        if kwargs:
             for k in class_attr:
                val = kwargs.get(k)
                if val:
                    setattr(self, k, val)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        places = relationship('Place', backref='cities',
                              cascade='all, delete-orphan')
