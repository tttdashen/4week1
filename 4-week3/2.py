from sys import settrace
from threading import settrace_all_threads
from turtle import width


class Student():
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=value

s = Student()
s.set_score(80)
print(s.get_score())
#s.set_score(1000)
#print(s.get_score())

#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：


#1. 为什么直接暴露属性不好？
class Student:
    pass

s = Student()
s.score = 9999   # 随便赋值，完全无法控制
'''
✅ 简单。 ❌ 但是有大问题：

你完全无法限制 score 合法范围（比如 0-100）。

也无法控制类型（比如必须是整数）。'''

#2. 用 get_score() 和 set_score() 方法代替直接赋值
class Student:
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''
✅ 好处：

能检查分数合法性，防止错误数据进入对象。

❌ 问题：

使用起来麻烦！
要写 s.set_score(80)、s.get_score()，而不是简单的 s.score = 80、s.score。

'''
#3. 有没有办法既能控制又像属性一样简单？
'''
✅ 答案就是：引入 @property 装饰器。

它能让：

s.score = 80，自动调用 set_score() 的逻辑

print(s.score)，自动调用 get_score() 的逻辑

代码写得像直接操作属性，但内部其实是经过方法控制的。

'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score=80
print(s.score)
#既能像访问属性一样简洁，又能在背后控制数据合法性。

#5. 还可以做什么？定义只读属性！
class Student():
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2025-self._birth
#birth 是可读可写的（有 getter 和 setter）
#age 是只读的（只有 getter，没有 setter）
# 必须注意：属性名和内部实例变量名不能冲突！
'''
class Student(object):
    @property
    def birth(self):
        return self.birth  # 错误！！！
属性方法名：比如 birth

实例变量名：加 _ 前缀，比如 _birth

这样永远不会冲突！

'''
tlf = Student()
tlf.birth = 1997
print(tlf.birth)
print(tlf.age)

#举例self.birth self._birth区别
class Student:
    def __init__(self, birth):
        self._birth = birth  # 真正保存数据
     
    @property
    def birth(self):
        print('getter被调用了')  # 可以看到什么时候被调用
        return self._birth
s = Student(2000)

print(s.birth)  # ✅ 触发 @property，自动执行 birth()
print('_'*30)
print(s._birth) # ✅ 直接访问底层变量
print('_'*30)
'''
访问 | 触发什么 | 结果
s.birth | 触发 @property -> 执行 getter 方法 | 执行逻辑，返回值
s._birth | 普通变量访问 | 直接拿值，无执行逻辑
注意：外部永远只跟 birth 打交道，不直接碰 _birth！'''

#长宽使用
class Screen():
    def __init__(self):
        self._width=0
        self._height=0
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value <= 0:
            raise ValueError('width must be positive!')
        self._width = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value <= 0:
            raise ValueError('height must be positive!')
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height   # 只读属性，返回宽*高
#没有 @resolution.setter，所以是只读的。
#外部只能 print(s.resolution)，不能 s.resolution = xxx。
# 测试
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)

if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
