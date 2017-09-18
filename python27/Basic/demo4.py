#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 条件语句  循环语句

print "##############################  1. 条件语句"
a = 12
if a < 1:
    print 'a<1'
elif a < 20:
    print 'a 在 1 和 20 之间'
else:
    print 'a 大于等于 20'


print "##############################  2. 循环中带else判断"
# 循环中带判断,判断不会进行死循环,会执行一次
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"


print "##############################  3. for循环 list,使用索引方式"
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

print "Good bye!"


print "##############################  4. pass 语句"
# pass 是空语句 不做任何事情，一般用做占位语句
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块,只是占个位置,让代码正常执行'
   print '当前字母 :', letter

print "Good bye!"


print "##############################  5. List列表"


print "##############################  6. 元组"


print "##############################  7. 字典"