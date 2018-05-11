import sys


def start_api_server():
    return None


if __name__ == '__main__':
    sys.argv.append('0.0.0.0:8000')
    app = web.application()
