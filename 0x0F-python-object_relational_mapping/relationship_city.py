#!/usr/bin/python3
# Defs a City model in program.
# Inherits from SQLAlchemy Base and links to the MySQL table cities.

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Reps a city for a MySQL db.

    Attributes:
        id (sqlalchemy.Column): The city's id in program.
        name (sqlalchemy.Column): The city's name in program.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
