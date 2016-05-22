
import imp
import os


class PluginMount(type):

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            print('Setting up mount point cls')
            cls.plugins = []
        else:
            print('Add {} to mount point'.format(cls.__name__))
            cls.plugins.append(cls)


def init_plugin(dirs):

    assert isinstance(dirs, list)

    for dir in dirs:
        for filename in os.listdir(dir):
            modname, ext = os.path.splitext(filename)
            if ext == '.py':
                print('Found {}'.format(filename))
                file, path, desc = imp.find_module(modname, [dir])
                if file:
                    print('Importing {}'.format(file))
                    mod = imp.load_module(modname, file, path, desc)



class HelloPlugin(metaclass=PluginMount):

    def say_hello(self, cls):
        pass


class GoodbyePlugin(metaclass=PluginMount):

    def say_goodbye(self, cls):
        pass


