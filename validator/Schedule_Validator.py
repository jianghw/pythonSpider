from validator.Proxy_Validator import ProxyValidator

try:
    from queue import Queue
except:
    # from Queue import Queue
    pass

from urllib3 import ProxyManager


class ScheduleValidator(ProxyManager, object):
    """
    验证代理
    """

    def __init__(self):
        self.queue = Queue()
        self.proxy_dict = dict()
        pass

    def m_validator_proxy(self, thread_count=10):
        """
        创建线程列表
        :param thread_count:
        :return:
        """
        list_thread = list()
        for i in range(thread_count):
            list_thread.append(ProxyValidator(self.queue, self.proxy_dict))

        for t in list_thread:
            t.daemon = True
            t.start()

        for thread in list_thread:
            thread.join()
        pass

    def main(self):
        pass


if __name__ == '__main__':
    sv = ScheduleValidator()
    sv.main()
