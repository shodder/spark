
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from . import Base, Session
from .plugin import ModelPlugins
from .plugin import HelloPlugin
from .plugin import GoodbyePlugin


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    family_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship('Address', back_populates='users')

    query = Session.query_property()

    hellos = ModelPlugins(HelloPlugin)

    def say_hello(self):
        for hellos in self.hellos:
            hellos().say_hello()

    goodbyes = GoodbyePlugin.plugins

    def say_goodbye(self):
        for goodbye in self.goodbyes:
            goodbye().say_goodbye(self)


class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    house_num = Column(Integer, nullable=False)
    street = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)

    users = relationship('User', back_populates='address')

    query = Session.query_property()

    hellos = ModelPlugins(HelloPlugin)

    def say_hello(self):
        for hellos in self.hellos:
            hellos().say_hello()

    goodbyes = GoodbyePlugin.plugins

    def say_goodbye(self):
        for goodbye in self.goodbyes:
            goodbye().say_goodbye(self)

