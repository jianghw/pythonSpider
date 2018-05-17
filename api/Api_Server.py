from flask import Flask, render_template, url_for, redirect, request, abort

from utils.Util_Config import EnvConfig

app = Flask(__name__, template_folder='/home/jianghw/Projects/python/pythonSpider/templates')


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
    print('hello is me ')
    return render_template('index.html')


@app.route('/form/', methods=['GET', 'POST'])
def form_input():
    name = request.form.get('name')
    age = request.form.get('age')
    if name is None or name == '' or age is None or age == '':
        return abort(401)

    return redirect(url_for('bo'))


def run_api():
    conf = EnvConfig()
    app.debug = True
    app.run(host=conf.host_host, port=conf.host_port)
    pass


if __name__ == '__main__':
    run_api()
