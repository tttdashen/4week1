#Python对象是动态的，可以随时绑定实例属性。类可以有类属性，实例优先找自己的属性，找不到再找类的属性。

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90  # 动态给实例 s 绑定一个属性 score
'''
在 Python 中，对象（实例）可以随时添加新属性，并不是只能用 __init__() 里定义的。

这里 s.score = 90，就是在对象 s 身上动态绑定了一个新属性 score。

这和在定义类时写不写 score 无关，是 Python 动态性的体现。
'''
#什么是类属性
class Student(object):
    name = 'Student'   # 这是一个类属性
#属性 是直接定义在 class 里面的变量，不属于任何实例，只属于类本身。
#类的所有实例可以访问到类属性，但是本质上是从类那里读取的。

s = Student()
print(s.name)        # 没有s自己的name属性，去Student类找name
print(Student.name)  # 直接访问类的name属性
#所以 s.name 在实例 s 上找不到时，会去 Student 类上找 name。

s.name = 'Michael'  # 给实例 s 自己绑定一个 name 属性
print(s.name)       # 输出实例自己的 name：Michael
print(Student.name) # 类的 name 还是 'Student'
#当你给实例 s 赋值 s.name = 'Michael'，
#实例 s 有了自己的 name 属性，就屏蔽了类的 name 属性。
#但是类属性还在，只不过访问不到了，要用 Student.name 才能访问类属性。
del s.name          # 删除实例自己的 name 属性
print(s.name)       # 访问时又去找类的 name 属性了


#test：让 Student 类能自动统计创建了多少个学生对象，每创建一个实例，计数加1。
class Student():
    count = 0 # 类属性，用来统计创建了多少个Student实例
    def __init__(self,name):
        self.name=name
        Student.count +=1# 每实例化一次，就让 count 加1

if Student.count!=0:
    print('测试失败')
else:
    A = Student('tlf')
    if Student.count!=1:
        print('测试失败')
    else:
        B=Student('tanlongfei')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')       

#实例属性属于各个实例所有，互不干扰；

#类属性属于类所有，所有实例共享一个属性；

#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

