#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 时间函数

print "##############################  1. time时间模块"
# 时间间隔是以秒为单位的浮点小数
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示

import time  # 引入 time 时间模块

a = time.time()
print '当前时间戳:' + str(a)

print "##############################  2. 时间元组"
# 用一个元组装起来的9组数字处理时间:
localtime = time.localtime(time.time())
print "本地时间为 :", localtime

print "##############################  3. 格式化时间"
# 可读的时间模式的函数是asctime()
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime

# 使用 time.strftime(format[, t]) 来格式化时间

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# 将格式字符串转换为时间戳
a = "Mon Sep 18 06:32:40 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


print "##############################  4. 获取日历 Calendar"

import calendar # 引入日历模块

cal = calendar.month(2017, 9)
print "以下输出2017年9月份的日历:"
print cal


print "##############################  5. datetime模块"


print "##############################  6. pytz模块"


print "##############################  7. dateutil模块"



