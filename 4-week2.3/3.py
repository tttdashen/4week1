#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal():
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()#对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
dog.run()
cat = Cat()
cat.run()
#继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animal实现了run()方法，
# 因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：

class Dog(Animal):
    def run(self):
        print('Dog is runnning...')
    def eat(self):
        print('Eating meat...')
dog=Dog()
dog.run()

#多态：当子类和父类都存在相同的run()方法时，我们说，
# 子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

#当我们定义了一个class时，我们实际上就定义了一种数据类型，和Python自带的数据类型，比如str、list、dict没什么两样：
a = list()
b = Animal()
c = Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))#看来c不仅仅是Dog，c还是Animal！
print(isinstance(b,Dog))#所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
#要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：

def run_twice(animal):
    animal.run()
    animal.run()
#当我们传入Animal的实例时，run_twice()就打印出：

run_twice(Animal())

#当我们传入Dog的实例时，run_twice()就打印出：

run_twice(Dog())

#看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
#你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

#继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。