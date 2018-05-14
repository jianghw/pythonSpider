from flask import Flask

from utils.Util_Config import EnvConfig

app = Flask(__name__)


def start_api_server():
    return None


def run_api():
    conf = EnvConfig()
    app.run(host=conf.host_host(), port=conf.host_port())
    pass


if __name__ == '__main__':
    run_api()
