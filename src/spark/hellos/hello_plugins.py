
from spark.model import User
from spark.model import Address
from spark.plugin import HelloPlugin


DISCRETES = {}

def register(model):

    def inner(cls):
        print(cls)
        print(model)
        DISCRETES[model] = cls
        return cls

    return inner


class HelloModel(HelloPlugin):

    def __init__(self, model):
        self.model = model

    def say_hello(self):
        print('I got {} so...'.format(self.model))
        print(type(self.model))
        DISCRETES[type(self.model)](self.model).say_hello()



@register(User)
class UserHello():

    def __init__(self, user):
        self.user = user
        pass

    def say_hello(self):
        print('Hello {} {}'.format(
            self.user.first_name, self.user.family_name))


@register(Address)
class AddressHello():

    def __init__(self, address):
        self.address = address
        pass

    def say_hello(self):
        print('Lives at {} {}'.format(
            self.address.house_num, self.address.street))


