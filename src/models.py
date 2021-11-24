import os
import datetime
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    mass = Column(String(250))
    skin_color = Column(String(250))
    height = Column(Integer)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    gravity = Column(String(250))
    population = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    object_type = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')