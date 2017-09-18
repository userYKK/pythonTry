#coding=utf-8
total=True
if total:
    # \ 是换行必须的
    str = "换行-"+\
          "换行-"+\
          "换行是用\\"
    print str
else:
    print "假"


"""
3个双引号的多行注释
"""
'''
3个单引号的多行注释
'''

# 等待用户输入； 同一行写多段代码需要使用 分号
name = raw_input("用户输入");print name