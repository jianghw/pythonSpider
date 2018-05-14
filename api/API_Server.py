from flask import Flask

app = Flask(__name__)


def start_api_server():
    return None


def run_api():
    app.run(host='', port='12')
    pass


if __name__ == '__main__':
    run_api()
