import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Data modeling starWars

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_name = Column(String(250))
    planets_population = Column(Integer)
    planets_diameter = Column(Integer)
    planets_rotation_period = Column(Integer)
    planets_climates = Column(String(250))
    planets_terrain = Column(String(250))


    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_name = Column(String(250))
    characters_hair_color = Column(String(250))
    characters_skin_color = Column(String(250))
    characters_eye_color = Column(String(250))
    characters_gender = Column(String(250))
    characters_mass = Column(Integer)
    characters_height = Column(Integer)

    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    # relationship me permite acceder a otras columnas de la tabla con la cual tengo la relacion
    fav_user = relationship(User)
    fav_planets = relationship(Planets)
    fav_characters = relationship(Characters)

    def to_dict(self):   
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')