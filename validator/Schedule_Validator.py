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

    def m_validator_proxy(self, thread_count=5):
        """
        创建验证线程列表
        :param thread_count:
        """
        list_thread = list()
        for i in range(thread_count):
            list_thread.append(ProxyValidator(self.queue, self.proxy_dict))

        for t in list_thread:
            t.daemon = True
            t.start()

        for thread in list_thread:
            thread.join()

    def main(self):
        self.m_put_queue()

        if not self.queue.empty():
            self.m_validator_proxy()

    def m_put_queue(self):
        """
        往队列中放ip
        """
        self.proxy_dict = dict()
        list_ip = self.db.select_db(
            'select ip_name from {table_name}'.format(table_name=self.db.all_proxy_name()))
        for ip in list_ip:
            self.queue.put(ip)


def run_validator():
    s_validator = ScheduleValidator()
    s_validator.main()


if __name__ == '__main__':
    sv = ScheduleValidator()
    sv.main()
