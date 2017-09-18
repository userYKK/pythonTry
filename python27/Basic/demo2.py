#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 变量类型

print "##############################  1. 多个变量赋值";
a = b = c = 1
print c

a, b, c = 'a', 2, '不同方式的初始化'
print c

print "##############################  2. 标准数据类型";
print 'Number, String, List, Tuple, Dictionary'
a, b, c = 1, 1.0, "字符串"
ta = type(a)
tb = type(b)
tc = type(c)
print ta
print tb
print tc

# python支持的数字类型: int long float  complex(复数)
a = 1 + 5j;
b = complex(2, 1.1)
print a
print b

print "##############################  3. 删除对象引用";
# 删除以后不能 print 等
a, b = 1, '字符串'
del a

print "##############################  4. 字符串"
# 正序从 0 开始 ,倒序从-1 开始
str = "abcd ef"
print str[3]  # 获取某一个字符
print str[0:3]  # 截取字符串,3下标不获取
print str[-4:]  # 倒序截取字符串，-1表示最后(或者不写),-4表示d
print str * 2  # 字符串重复2次
print str + "拼接"  # 字符串的拼接
print str[::-1]  # 对str的取反
print str[:-5]  # 截取从头开始到倒数第 5 个字符(包括这个,-1 开始)
print str[:-5:-3]  # 逆序截取 格式: str[begin:end:step]
# begin,起始位置
# end, 结束位置
# step,间隔.s不等于0.默认为1
# 区间为左闭右开.
# step>0,表示从左往右.
# step<0,表示从右往左.


print "##############################  5. List列表"
list = ['runoob', 786, 2.23, 'john',
        [
            'a1', 'a2'
        ]

        ]
tinylist = [123, 'john']

print list[0]
print list[4][1]
print list[1:3]          # 输出第二个至第三个的元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表


print "##############################  6. 元组"
# 使用()是只读的,不能二次赋值
tuple = (1,'字符串',1.1)

print tuple[1]


print "##############################  7. 字典"
# 无序的 key-value
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

print dict


