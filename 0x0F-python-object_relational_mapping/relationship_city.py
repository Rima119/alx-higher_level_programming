#!/usr/bin/python3
"""
City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """City class
    Attributes:
       id (int): id of the city.
       name (str): name of the city.
       state_id (int): id of the associated state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
