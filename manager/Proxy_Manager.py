from db.Db_Factory import DbFactory
from utils.Util_Config import EnvConfig
from utils.Util_Log import UtilLogger


class ProxyManager(object):
    """
    操作代理db
    """

    def __init__(self):
        self.db = DbFactory()
        self.log = UtilLogger()
        self.conf = EnvConfig()
        pass


if __name__ == '__main__':
    pass
