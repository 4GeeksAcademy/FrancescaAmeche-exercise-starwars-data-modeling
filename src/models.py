import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name= Column(String(250), nullable=False)
    email = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type_of_favorite = Column(String(250), nullable=False)
    people_id= Column(String(250), ForeignKey('people.id'), nullable=True)
    planet_id= Column(String(250), ForeignKey('planets.id'), nullable=True)
    starship_id= Column(String(250), ForeignKey('starships.id'), nullable=True)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))
    mass = Column(Integer)
    height = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(Integer)
    population = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    surface_water= Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(Integer)
    length = Column(Integer)
    consumables = Column(String(250))
    cost_in_credits = Column(Integer)
    crew= Column(Integer)
    passengers= Column(Integer)
    hyperdrive_rating= Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
