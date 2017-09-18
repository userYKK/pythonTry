#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件 I/O

print "##############################  1. raw_input函数,input函数"
print ' input 可以接收一个Python表达式作为输入，并将运算结果返回'

print "##############################  2. open打开文件,close(),File文件操作,OS文件夹/目录操作"
fo = open("tempDel.py", "rb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

fo.close()
print "是否已关闭 : ", fo.closed


print "##############################  3. 删除对象引用"


print "##############################  4. 异常抓取"
try:
    fh = open("testfile", "r")
    fh.read()
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
finally:
    print '最后清尾工作'


print "##############################  5. 触发异常"
a = 1
try:
    raise Exception("Invalid level!", a)
except Exception,e:
    print e.args


print "##############################  6. 自定义异常"
# 自定义的异常类
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print e.args

