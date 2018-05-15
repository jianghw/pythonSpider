class Singleton(type):
    """
        单例
        """
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._inst[cls]


class LazyProperty(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


try:
    from configparser import ConfigParser  # py3
except Exception as err:
    # from ConfigParser import ConfigParser  # py2
    pass


class ApiConfigParser(ConfigParser):
    """
        做py3&&py2 兼容
        """

    def __init__(self):
        super(ConfigParser, self).__init__()
