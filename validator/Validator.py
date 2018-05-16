import json
import time

import requests
from requests import HTTPError, TooManyRedirects, RequestException

from utils import Util_Config


def _check_http_proxy(self, proxy_dict, isHttp=True):
    """
    检查代理状态
    :param self:
    :param proxy_dict: 开始工作的代理点
    :param isHttp: 是否安全请求
    :return: 只有成功时 True、2/1/0、speed
    """
    req_types = -1
    req_speed = -1

    if isHttp:
        url_test = Util_Config.TEST_HTTP_HEADER
    else:
        url_test = Util_Config.TEST_HTTPS_HEADER

    start = time.time()

    try:
        rsp = requests.get(url=url_test, headers=Util_Config.get_header(),
                           timeout=Util_Config.TIME_OUT,
                           proxies=proxy_dict)
        if rsp.ok:
            rsp_json = json.loads(rsp.text)
            print(rsp_json)
            headers = rsp_json['headers']
            origin = rsp_json['origin']
            proxy_conn = headers.get('Proxy-Connection', None)
            if ',' in origin:
                req_types = 2
            elif proxy_conn:
                req_types = 1
            else:
                req_types = 0
            req_speed = round(time.time() - start, 2)
            return True, req_types, req_speed
        else:
            return False, req_types, req_speed

    except ConnectionError as error:
        print(error)
    except HTTPError as error:
        print(error)
    except TooManyRedirects as error:
        print(error)
    except RequestException as error:
        print(error)
    finally:
        return False, req_types, req_speed


# {"origin":"116.231.57.49"}
def get_my_ip():
    rsp = requests.get(url=Util_Config.URL_ID_REQUEST,
                       headers=Util_Config.get_header(),
                       timeout=Util_Config.TIME_OUT)
    return rsp.text


if __name__ == '__main__':
    # ip = '180.173.69.71'
    # port = '9797'
    # proxy_dict = {
    #     'http': 'http://%s:%s' % (ip, port),
    #     'https': 'https://%s:%s' % (ip, port)
    # }
    # _check_http_proxy(None, proxy_dict)

    get_my_ip()
    pass
