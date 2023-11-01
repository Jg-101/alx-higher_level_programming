#!/usr/bin/python3
# Defs a State model in program.
# Inherits from SQLAlchemy Base and links to the MySQL table states in program.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Reps a state for a MySQL dbase.

    Attributes:
        __tablename__ (string): The name of the MySQL table to store States.
        id (sqlalchemy.Int): The state's id.
        name (sqlalchemy.Str): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
