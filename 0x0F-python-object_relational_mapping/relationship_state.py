#!/usr/bin/python3
"""
State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(Base):
    """State class
    Attributes:
       id (int): id of the state.
       id of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
