#!/usr/bin/python
#coding=utf-8

from flask import Flask
from flask import request
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 路径参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

# 获取浏览器代理
@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    print user_agent
    return '<p>您的浏览器是: %s</p>'%user_agent
    # return '<p>your browser is: %s</p>'%user_agent

if __name__ == '__main__':
    app.run(debug=True)
