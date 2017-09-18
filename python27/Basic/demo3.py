#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 运算符

print "##############################  1. 算术运算符"
# 幂运算
# 取整除
a = 2 ** 2
b = 10//3
c = 11.0//2

print a
print b
print c


print "##############################  2. 逻辑运算符"
a = 1 and 0
b = 1 or 0
c = 1 and 22

print a
print b
print c

print "##############################  3. 成员运算符"
# in   not in 运算
list = [1, 2, 3, 4, 5 ]
a = 1 in list
b = 10 in list
c = 1 not in list

print a
print b
print c


print "##############################  4. 身份运算符"
# is  is not 运算符 --- 判断2个标识符是否引用同一个对象
#  is 和  == 区别 ： 后面一个判断变量的值是否相等
list = [1, 2, 3, 4, 5 ]
list2 = [1, 2, 3, 4, 5 ]
list3 = list

num1 = 10
num2 = 10

a = list is list2
b = list is list3
c = list2 is list3
d = list == list2
e = num1 is num2

print a
print b
print c
print d
print e

