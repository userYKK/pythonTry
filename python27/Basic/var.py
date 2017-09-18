#coding=utf-8
# 1. 单个变量的赋值
count = 1
print count
# 2. 多个变量的赋值
a = b = c = 2
print b
d,e,f = 3,4,"python真逗逼"
print f

# 3. python中的数字变量--数值变量的修改和删除指向
num1 = 1
num2 = num1
del num1  #删除num1，那么后面就回去不到num1这个数值对象
print num2

# 4. 字符串 --- 倒序从-1 开始
str = "abcd ef"
print str[3]  #获取某一个字符
print str[0:3] #截取字符串，3下标不获取
print str[-4:] #倒序截取字符串，-1表示最后(或者不写),-4表示d
print str*2  #字符串重复2次
print str + "拼接" #字符串的拼接
print str[::-1]  #对str的取反
print str[:-5]
print str[:-5:-3]