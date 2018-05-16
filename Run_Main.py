from multiprocessing import Process

from api import Api_Server
from validator import Schedule_Validator

if __name__ == '__main__':
    list_pro = list()
    process_api = Process(target=Api_Server.run_api(), name='run_api')
    list_pro.append(process_api)
    process_validator = Process(target=Schedule_Validator.run_validator(),
                                name='run_validator')
    list_pro.append(process_validator)

    for process in list_pro:
        process.daemon = True
        process.start()

    for pro in list_pro:
        pro.join()

    pass
