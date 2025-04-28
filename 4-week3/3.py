from signal import raise_signal


class Student():
    def __init__(self,name):
        self.name=name
print(Student('tlf'))#打印出一堆<__main__.Student object at 0x109afb190>，不好看。

class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Stuedent Object (name:%s)'% self.name
print(Student('tlf'))


#1.__iter__  让对象可以 for 循环
'''
作用
让你的对象支持 for ... in 语法，像 list、tuple 那样一项一项迭代。

必须实现：

__iter__(self) 返回一个迭代器对象

这个迭代器对象内部必须有 __next__() 方法'''

class Fib:
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
'''
内容 | 说明
__iter__() | 返回一个迭代器对象
__next__() | 返回下一个元素，遇到 StopIteration 停止'''

#2.__getitem__：让对象像列表一样通过索引访问
'''
让你的对象支持 obj[n] 这种按下标访问。

必须实现 __getitem__(self, n) 方法。

n 可能是整数（单个元素），也可能是 slice（切片）。


'''
class Fib():
    def __getitem__(self,n):
        a,b=1,1
        for _ in range(n):
            a,b=b,a+b
        return a
f = Fib()
print(f[5])   # 输出斐波那契第6项


#支持切片的改进版
class Fib():
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for _ in range(n):
                a,b=b,a+b
            return a
        if isinstance(n, slice):
            start = n.start or 0
            stop = n.stop
            L = []
            a, b = 1, 1
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        

#3. __getattr__：动态返回不存在的属性
'''
作用
当访问对象一个不存在的属性时，会自动调用 __getattr__(self, attr)。

你可以在里面动态返回任何值、方法，或者抛出异常。'''
class Student:
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError(f"'Student' object has no attribute '{attr}'")
s = Student()
print(s.name)    # 直接访问存在的属性
print(s.score)   # 动态生成的属性
print(s.age())   # 动态生成的方法
print(s.abc)     # 抛异常
#4. __call__：让对象像函数一样调用
class Student:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"My name is {self.name}.")
s = Student('Michael')
s()   # 直接调用实例本身

'''
定制方法 | 作用 | 主要用在什么场景？
__iter__ + __next__ | 支持 for循环 | 自定义可迭代对象
__getitem__ | 支持 obj[n] 访问 | 像列表、字典那样用对象
__getattr__ | 动态返回不存在属性 | 动态构建属性、链式调用API
__call__ | 让对象能被()调用 | 对象当成函数'''