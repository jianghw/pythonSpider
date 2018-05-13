from multiprocessing import Process
from queue import Queue

from utils import IP_Config
from api import API_Server
from validator import Validator

if __name__ == '__main__':
    my_ip = Validator.get_my_ip()
    q_list = Queue(maxsize=IP_Config.TASK_QUEUE_SIZE)
    process = Process(target=API_Server.start_api_server,)

    pass
