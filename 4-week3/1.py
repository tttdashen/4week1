class Student():
    pass
s = Student()

s.name = 'tlf'#尝试给实例绑定一个属性
print(s.name)

#尝试给实例绑定一个方法：
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)
print(s.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
#print(s2.set_age(25))  ---会报错
#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score =score
Student.set_score = set_score
s.set_score(100)
print(s.score)

a=Student()
a.set_score(200)
print(a.score)


#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
'''
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

'''
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
