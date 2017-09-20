#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 类

print "##############################  1. 类定义"
class Code:
    count = 1

    # 构造函数
    def __init__(self):
        self.count = 2
        self.other = 'other 变量初始化在构造函数'
        # 直接使用类调用 -- 这个和实例的count是不一个count
        Code.count = 3

        print self.count
        print self.other

# 实例化类
parent = Code()
print Code.count

print "##############################  2. 类中函数会把第一个参数绑定在实例上面"
class Type:
    param1 = 1
    def __init__(self):
        self.param1 = 2

    # 获取class以及实例信息
    def getClassInfo(self):
        # 查看self的指向
        print self
        # 查看__class__ 指向的类本身
        print self.__class__


type = Type()
type.getClassInfo()

print "##############################  3. 类的一些内置属性"
class ClassInfo:
    '这部分是类的注释'
    count = 1

    def getInfo(self,info):
        """
            getInfo 的方法的描述
        """
        # 实例获取类的文档字符串
        print self.__doc__
        print self.__module__


classInfo = ClassInfo()
classInfo.getInfo('测试参数')

# 获取类的属性

# 获取文档字符串
print ClassInfo.__doc__
# 获取类名
print ClassInfo.__name__
# 获取类所在的模块
print ClassInfo.__module__
# 所有父类
print ClassInfo.__bases__
# 获取类的属性,是一个字典
print ClassInfo.__dict__


print "##############################  4. 析构函数"
class Point:
    def __init__(self):
        print '默认构造函数'

    def __del__(self):
        print '类的析构函数'

point = Point()
# 删除实例时候会调用析构函数
del point


print "##############################  5. 类的继承 -- super 或者 类直接调用 (最好统一)"
# 可以多重集成
# 在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
# 在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
# 先在本类中查找调用的方法，找不到才去基类中找

class Parent(object):
    parentCount = 1
    def __init__(self):
        print 'Parent 的 init 方法'

    def getInfo(self):
        print 'Parent 的 getInfo 方法'


class Child(Parent):
    childCount = 2
    def __init__(self):
        # Parent.__init__(self)
        # super(Parent,self).__init__()
        print 'Child 的 init 方法'

    def getInfo(self):
        print 'Child 的 getInfo 方法'
        super(Child, self).getInfo()

    def getOther(self):
        print 'Child 的 getOther 方法'

child = Child()
child.getOther()
child.getInfo()


print "##############################  6. mro 的简单使用"

class ChildA(object):
  def foo(self):
    print '--ChildA--'

class ChildB(ChildA):
  def foo(self):
    print '--ChildB--'
    # super(ChildB, self).foo()

class ChildC(ChildA):
  def foo(self):
    print '--ChildC--'
    super(ChildC, self).foo()

class ChildD( ChildC,ChildB):
  def foo(self):
    print '--ChildD--'
    super(ChildD, self).foo()

ChildD().foo()
print ChildD.mro()
print "##############################  7. 字典"
