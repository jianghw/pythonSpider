from flask import Flask

from utils.Util_Config import EnvConfig

app = Flask(__name__)


def start_api_server():
    return None


dict_api = {
    'get': u'get an unable proxy',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
    'get_status': u'proxy statistics'
}


@app.route('/')
def index():
    return 'hello flask'


def run_api():
    conf = EnvConfig()
    app.debug = True
    app.run(host=conf.host_host, port=conf.host_port)
    pass


if __name__ == '__main__':
    run_api()
