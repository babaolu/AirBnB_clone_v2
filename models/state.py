#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    def __init__(self, *args, **kwargs):
        """ Setting up initialization for the State class
            *args: Is not been used
        """
        super().__init__(**kwargs)
        class_attr = ["name"]
        self.name = ""
        if kwargs:
            for k in class_attr:
                val = kwargs.get(k)
                if val:
                    setattr(self, k, val)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Gets cities from FileStorage"""
            from models import storage

            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
