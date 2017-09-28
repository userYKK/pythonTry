#!/usr/bin/python
#coding=utf-8

from flask import Flask
from flask import request
from flask import  redirect
from flask import abort

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


# 获取这个app的所有的路由:
#   1. 在app所在的目录下面 from hello import app
#     2.  app.url_map 就可以看 app 定义的所有的路由



# 设置服务器的response响应吗
@app.route('/getResponse')
def getResposeCode():
    return '<h1>Bad Request error  400</h1>', 400

# 设置重定向
@app.route('/redirectRoute')
def redirectRoute():
    return redirect('http://www.baidu.com')

# 测试abort设置response,调用web容器自己的 404 页面
@app.route('/getAbort')
def getAbort():
    abort(404)


# 原始的系统启动
# if __name__ == '__main__':
#     app.run(debug=True)

from flask.ext.script import Manager
manager = Manager(app)

# script 代理启动,使用 python hello.py runserver --host 0.0.0.0 启动
if __name__ == '__main__':
    manager.run()

