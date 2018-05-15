from utils.Util_Config import EnvConfig


class DbClient:
    def __init__(self):
        self.conf = EnvConfig()
        self.__init_db_client()

    def __init_db_client(self):
        __db_type = None
        if 'sqlite' == self.conf.db_type:
            __db_type = 'Sqlite_Client'
        assert __db_type, 'db type is error {}'.format(self.conf.db_type)
        self.client = getattr(__import__(__db_type), __db_type)(name=self.conf.db_name,
                                                                host=self.conf.db_host,
                                                                port=self.conf.db_port)


if __name__ == '__main__':
    db = DbClient()
    pass
