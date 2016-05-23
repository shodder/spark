
from spark.model import User
from spark.model import Address
from spark.plugin import GoodbyePlugin

DISCRETES = {}

def register(model):

    def inner(cls):
        print(cls)
        print(model)
        DISCRETES[model] = cls
        return cls

    return inner


class GoodbyeModel(GoodbyePlugin):

    def __init__(self):
        pass

    def say_goodbye(self, model):
        print('I got {} so...'.format(model))
        print(type(model))
        DISCRETES[type(model)]().say_goodbye(model)



@register(User)
class UserGoodbye():

    def __init__(self):
        pass

    def say_goodbye(self, user):
        print('say_goodbye {} {}'.format(
            user.first_name, user.family_name))


@register(Address)
class AddressGoodbye():

    def __init__(self):
        pass

    def say_goodbye(self, address):
        print('Is moving out of {} {}'.format(
            address.house_num, address.street))
