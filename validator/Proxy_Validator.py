from threading import Thread

import requests

from manager.Proxy_Manager import ProxyManager
from utils import Util_Config


def _verify_http(ip_dict, http=True):
    if http:
        proxies = ip_dict['http']
    else:
        proxies = ip_dict['https']

    url_ip = Util_Config.URL_ID_REQUEST
    rsp = requests.get(url=url_ip, headers=Util_Config.get_header(),
                       timeout=Util_Config.TIME_OUT, proxies=proxies, verify=False)
    if rsp.status_code == 200:
        return True
    else:
        return False


def verify_valid_ip(proxy_ip):
    ip = ''
    port = ''
    ip_dict = {
        'http': 'http://{ip}:{port}'.format(ip=ip, port=port),
        'https': 'https://{ip}:{port}'.format(ip=ip, port=port)
    }
    return _verify_http(ip_dict)


class ProxyValidator(ProxyManager, Thread):
    """
    代理验证线程
    """

    def __init__(self, queue, proxy_dict):
        # ProxyValidator.mro()
        super(ProxyValidator, self).__init__()
        self.queue = queue
        self.proxy_dict = proxy_dict
        pass

    def run(self):
        while self.queue.qsize():
            proxy_ip = self.queue.get()
            proxy_count = self.proxy_dict['ip']
            if verify_valid_ip(proxy_ip):
                pass
            else:
                pass

        pass


if __name__ == '__main__':
    # p = ProxyValidator(Queue(), dict())
    print(ProxyValidator.mro())
    pass
