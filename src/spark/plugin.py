
from functools import partial
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


class ModelPlugins(object):

    def __init__(self, mounted_plugin):
        print('ModelPlugins descriptor for {}'\
            .format(mounted_plugin))
        self.mounted_plugin = mounted_plugin

    def __get__(self, model, owner):
        print('ModelPlugins __get__ {}, {}'.format(
            model, owner))

        return [partial(p, model) for p in self.mounted_plugin.plugins]


def init_plugin(dirs):

    assert isinstance(dirs, list)

    for dir in dirs:
        for filename in os.listdir(dir):
            modname, ext = os.path.splitext(filename)
            if ext == '.py':
                if modname[:2] == '__':
                    continue

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


