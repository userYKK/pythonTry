#!/usr/bin/python
# -*- coding: UTF-8 -*-
#  基础语法的学习

print "##############################  1. 中文处理方式";
# 或者直接使用   #coding=utf-8 也可以
print  "中文处理方式"

print "##############################  2. 标识符";
#    _foo 表示不能直接访问的类属性,不能使用 from xxx import *  导入
#    __foo__ python中特殊方法专用的标志 : __init__() 表示类的构造函数


print "##############################  3. 多行语句";
#    使用 \ 表示
#    [] {} () 不需要多行连接符

total = '11' + \
        '22' + \
        '33';
print total;

days = ['a1', 'a2'
              'a2'];
print days;

print "##############################  4. python 中引号"
word = '单引号'
sentence = "双引号"
paragraph = """三个双引号表示一个段落,可以换行,
不需要换行符"""

paragraph_1 = '''三个单引号也表示段落,
也不需要换行符'''

print word
print sentence
print paragraph
print paragraph_1

print "##############################  5. python注释"
#    python中的注释,多行注释可以使用三个双引号(或者单引号)
'''
这部分是注释
11
'''

print "##############################  6. 等待用户输入"
content = raw_input("请输入内容:")
print content

print "##############################  7. 同行编写多条语句"
import sys;

x = "使用sys模块打印";
sys.stdout.write(x + "\n")

print "##############################  8. 显示时候不换行输出信息"
print "第一行",
print "第二行"
