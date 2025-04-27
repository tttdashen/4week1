#获取对象信息

#基本类型都可以用type()判断：
print(type(134))
print(type('123'))
print(type(None))
#如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
print(type(1))
'''
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False
'''
#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
from ssl import HAS_SNI
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(1,10)))==types.GeneratorType)

'''
使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

我们回顾上次的例子，如果继承关系是：

object -> Animal -> Dog -> Husky
那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
然后，判断：

>>> isinstance(h, Husky)
True
没有问题，因为h变量指向的就是Husky对象。

再判断：

>>> isinstance(h, Dog)
True
h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也还是Dog类型。换句话说，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

因此，我们可以确信，h还是Animal类型：

>>> isinstance(h, Animal)
True
同理，实际类型是Dog的d也是Animal类型：

>>> isinstance(d, Dog) and isinstance(d, Animal)
True
但是，d不是Husky类型：

>>> isinstance(d, Husky)
False
能用type()判断的基本类型也可以用isinstance()判断：

>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
 提示

总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
'''

#第一步：查看对象的所有属性和方法 → 用 dir()
print(dir('ABC'))
#dir() 返回的是字符串列表，列出对象拥有的所有属性名和方法名（包括特殊方法）。

#第二步：了解什么是特殊方法 → __xxx__ 形式
print(len('ABC'))
print('ABC'.__len__())

#第三步：自定义类也可以有特殊方法（重写 __len__）
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

#第四步：普通方法调用示例 → 比如 lower()
print('ABC'.lower())

#第五步：动态操作对象属性 → 用 hasattr() / getattr() / setattr()
class Myobject():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x

obj = Myobject()
#1️⃣ 判断是否有某个属性 → hasattr()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))

#2️⃣ 动态设置属性 → setattr()
setattr(obj,'y',30)
#这时，obj 对象就多了一个 y 属性。

#3️⃣ 动态读取属性 → getattr()
print(getattr(obj,'y'))
print(getattr(obj, 'z', 404)) # 属性不存在，返回 404

#4️⃣ 动态操作方法
#判断是否有方法：
hasattr(obj,'power')
#拿到方法（注意，不是执行！）：
fn=getattr(obj,'power')
print(fn)
#执行方法：
print(fn())

#总的步骤
# 定义一个类 MyObject
class MyObject(object):
    def __init__(self):
        self.x = 9    # 定义一个属性 x，初始值为 9

    def power(self):
        return self.x * self.x    # 定义一个方法 power，返回 x 的平方

# 创建实例对象 obj
obj = MyObject()

# 1. 判断对象有没有属性 'x'
print(hasattr(obj, 'x'))    # 输出 True，因为 __init__ 里定义了 x

# 2. 读取属性 'x'
print(obj.x)                # 直接访问，输出 9

# 3. 判断对象有没有属性 'y'
print(hasattr(obj, 'y'))    # 输出 False，因为目前没有 y 属性

# 4. 动态添加属性 'y'，并赋值为 19
setattr(obj, 'y', 19)

# 5. 再次判断有没有属性 'y'
print(hasattr(obj, 'y'))    # 输出 True，现在有了 y

# 6. 获取属性 'y' 的值
print(getattr(obj, 'y'))    # 输出 19
print(obj.y)                # 直接访问，输出 19

# 7. 获取一个不存在的属性 'z'（不加默认值会报错）
# print(getattr(obj, 'z'))   # ❌ 这行如果直接运行，会报 AttributeError

# 8. 获取一个不存在的属性 'z'，并设置默认值
print(getattr(obj, 'z', 404))  # 输出 404，因为 z 不存在，返回默认值

# 9. 判断对象有没有方法 'power'
print(hasattr(obj, 'power'))  # 输出 True，power 是一个方法

# 10. 获取方法 'power'，并调用
fn = getattr(obj, 'power')   # 注意：这里拿到的是方法对象（不是执行结果）
print(fn)                    # 打印方法的描述
print(fn())                  # 调用方法，输出 81

'''
Python 内置的一些函数（比如 dir()、hasattr()、getattr()、setattr()）

可以用来动态查看和操作对象内部的数据或方法。

但是如果你明确知道对象有什么属性，就直接用点号.访问，不要多此一举用动态的函数去访问。

动态操作（比如 getattr）适合在对象内容不确定的情况下使用。

鸭子类型理念：不是看对象的真实身份，而是看它有没有特定的方法，能不能完成任务。只关心"能干活"，不关心"长啥样"！


'''