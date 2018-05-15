from db.Db_Client import DbClient
from utils.Util_Log import UtilLogger


class ProxyManager(object):
    """
    操作代理db
    """

    def __init__(self):
        self.db = DbClient()
        self.log = UtilLogger()
        pass


if __name__ == '__main__':
    pass
