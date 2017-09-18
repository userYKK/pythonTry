__author__ = 'ykk'
#coding=utf-8
# 在 goog.closure 找到一个父类的所有的子类

# 1. 读取所有的内容
# all_the_text = open(folder + filename).read();

# 2. 逐行读取,匹配对应的文本并且显示
def findLine(f,inheritStr,searchStr):
    file=open(f)
    line=file.readline()
    count=0
    childrenList = []
    while line:
        count += 1
        # print line
        line=file.readline()
        # 判断当前行是有继承设置的
        if(inheritStr in line):
            # 判断确实是继承指定的类的
            line = line.replace(" ","")
            if(searchStr in line):
                # 打印出当前的文件
                print f
                test = str(count) + " : " + line
                print test
                # childrenList.append(count + " : " + line)
                break
    file.close()
    # 利用for循环遍历列表中的元素
    # for item in childrenList:
    #     print item


# 3. 递归所有的文件
def findJS(directory,inheritStr,searchStr):
    for fpathe,dirs,fs in os.walk(directory):
        # fpathe: 文件夹的路径
        # print fpathe
        # dirs: 查找的方式,root中找到指出所有的 dir文件夹，然后进入第一个文件夹列出 dir,并且每一个dir都进入看
        # print dirs
        # dirs: 所有的文件
        # print fs
        for f in fs:
            jsFile = file_extension(f)
            if(jsFile==".js"):
                jsPath = os.path.join(fpathe,f)
                findLine(jsPath,inheritStr,searchStr)

# 4. 获取文件的文件后缀名
def file_extension(path):
  return os.path.splitext(path)[1]

#  5. 获取命令行的参数
def getParam(folder,inheritStr,searchStr):
    # 脚本名称
    print sys.argv[0]
    # 参数的个数
    # print len(sys.argv)
    if len(sys.argv) > 1 :
        for i in range(1, len(sys.argv)):
            # print "参数", i, sys.argv[i]
            searchStr = sys.argv[1]+")"
            print searchStr
            findJS(folder,inheritStr,searchStr)
    else:
        print "pleace give me param --- searchKey"

# 函数的调用
import os
import sys

# folder="F://pp//"
folder="E://ykk//dev//worktemp//mi-web-tool//web//"
inheritStr="goog.inherits("
searchStr=""
getParam(folder,inheritStr,searchStr)
# findJS(folder,inheritStr,searchStr)


