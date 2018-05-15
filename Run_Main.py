from multiprocessing import Process
from queue import Queue

from utils import Util_Config
from api import Api_Server
from validator import Validator

if __name__ == '__main__':
    my_ip = Validator.get_my_ip()
    q_list = Queue(maxsize=Util_Config.TASK_QUEUE_SIZE)
    process = Process(target=Api_Server.run_api(), name='run_api')
    q_list.put(process)

    pass
