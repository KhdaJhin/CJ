# encoding: utf8
import config
from flask import Flask, render_template, send_file, request, url_for


app = Flask(__name__)


# @app.route('/hello')
# def hello_world():
#     return render_template('subject/jhin.html', Shakespeare=Shakespeare)


@app.route('/index')
def jhin():
    return '实验'


@app.route('/')
def hello():
    return render_template('dev/gg.html')


@app.template_global()
def ab(a, w):
    return a + w


@app.route('/rng')
def uu():
    return render_template('yunsuan.html')


@app.route('/albert')
def albert():
    return render_template('blog/albert.html')


if __name__ == '__main__':
    app.config.root_path(config)
    app.run(debug=True)
