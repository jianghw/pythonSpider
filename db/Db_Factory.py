import sqlite3

from utils.Util_Config import EnvConfig


class DbFactory:
    """
    db 服务工厂
    """

    def __init__(self):
        self.conf = EnvConfig()
        self.__init_db_client()

    def __init_db_client(self):
        __db_type = None
        if 'sqlite' == self.conf.db_type:
            __db_type = 'Sqlite_Client'
        assert __db_type, 'db type is error {}'.format(self.conf.db_type)

        self.client = getattr(__import__(__db_type), __db_type)(
            name=self.conf.db_name,
            host=self.conf.db_host,
            port=self.conf.db_port)

    def insert_db(self):
        pass

    def select_db(self):
        pass

    def where_db(self):
        pass

    def update_db(self):
        pass

    def all_proxy_name(self):
        return self.client.all_proxy_name()


if __name__ == '__main__':
    pass
