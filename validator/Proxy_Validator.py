from queue import Queue
from threading import Thread

from manager.Proxy_Manager import ProxyManager


class ProxyValidator(ProxyManager, Thread):
    """
    代理验证
    """

    def __init__(self, queue, proxy_dict):
        # ProxyValidator.mro()
        super(ProxyValidator, self).__init__()

        pass


if __name__ == '__main__':
    # p = ProxyValidator(Queue(), dict())
    print(ProxyValidator.mro())
    pass
