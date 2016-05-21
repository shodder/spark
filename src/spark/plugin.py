
class PluginMount(type):

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            print('Setting up mount point cls')
            cls.plugins = []
        else:
            print('Add {} to mount point'.format(cls.__name__))
            cls.plugins.append(cls)


class HelloPlugin(metaclass=PluginMount):

    def say_hello(self, cls):
        pass


class GoodbyePlugin(metaclass=PluginMount):

    def say_goodbye(self, cls):
        pass


