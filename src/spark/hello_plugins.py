
from spark.model import User
from spark.model import Address

from .plugin import HelloPlugin

DISCRETES = {}

def register(model):

    def inner(cls):
        print(cls)
        print(model)
        DISCRETES[model] = cls
        return cls

    return inner


class HelloModel(HelloPlugin):

    def __init__(self):
        pass

    def say_hello(self, model):
        print('I got {} so...'.format(model))
        print(type(model))
        DISCRETES[type(model)]().say_hello(model)



@register(User)
class UserHello():

    def __init__(self):
        pass

    def say_hello(self, user):
        print('Hello {} {}'.format(
            user.first_name, user.family_name))


@register(Address)
class AddressHello():

    def __init__(self):
        pass

    def say_hello(self, address):
        print('Lives at {} {}'.format(
            address.house_num, address.street))


