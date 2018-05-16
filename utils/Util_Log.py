import logging
from logging import Logger, DEBUG

import os
from logging.handlers import TimedRotatingFileHandler

CURRENT_LOG_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_LOG_PATH = os.path.join(CURRENT_LOG_PATH, os.path.pardir)
FILE_LOG_PATH = os.path.join(ROOT_LOG_PATH, 'logger')


class UtilLogger(Logger):
    def __init__(self, name='log', level=DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        super(UtilLogger, self).__init__(self.name, level=self.level)

        if stream:
            self.__set_stream_handler()
        if file:
            self.__set_file_handler()

    def __set_stream_handler(self):
        pass

    def __set_file_handler(self, level=None):
        file_name = os.path.join(FILE_LOG_PATH, '{name}'.format(name=self.name))

        time_rotating_handler = TimedRotatingFileHandler(file_name, when='d',
                                                         backupCount='15')
        if not level:
            time_rotating_handler.setLevel(self.level)
        else:
            time_rotating_handler.setLevel(level)

        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        time_rotating_handler.setFormatter(formatter)
        self.time_handler = time_rotating_handler
        self.addHandler(time_rotating_handler)


if __name__ == '__main__':
    print(CURRENT_LOG_PATH)
    print(ROOT_LOG_PATH)
    print(FILE_LOG_PATH)

    log = UtilLogger()
    log.info('hello it is test')
    pass
