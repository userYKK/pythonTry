#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 函数模块

print "##############################  1. 函数声明"
def printme( str ):
   "这部分是函数中的注释"
   print str
   return
printme('hehe')

print "##############################  2. 必备参数"
# 函数调用必须传递一个参数,否则会报错
def printme(str):
    print str
    return;

printme('必备参数');

print "##############################  3. 关键字参数"
# 关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printinfo(name, age):
    print "Name: ", name
    print "Age ", age
    return

# 可以参数顺序不同
printinfo(age=50, name="miki")


print "##############################  4. 缺省参数"
# 某一个参数在函数声明时候就有默认值
def printinfo(name, age=35):
    print "Name: ", name
    print "Age ", age
    return

printinfo(age=50, name="关键字设置2个参数");
printinfo(name="age使用默认参数");

print "##############################  5. 不定长参数"
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print arg1
    for var in vartuple:
        print var,
    return


printinfo(10)
print '-----'
printinfo(70, 60, 50)
print ''
print '-----'

print "##############################  6. 匿名函数 -- lambda 创建函数"

sum = lambda arg1, arg2: arg1 + arg2;
print "相加后的值为 : ", sum(10, 20)

print "##############################  7. globals()  locals()  reload() 函数"
# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次;想重新执行模块里顶层部分的代码，可以用 reload() 函数。
glob = '这个是全局变量'
def a():
    print '获取 globals'
    print globals()
    print '获取 locals'
    print globals()

a()