def power(x,n):
    s = 1
    while n>0:
        n= n-1
        s= s*x
    return s

a=power(5,3)
print(a)

# def powers(x,n):
#     s=x
#     while n>0:
#         n=n-2
#         s = x*s
#     return s
# b=powers(5,3)
# print(b)
#错误的，虽然5，3条件下和函数1为同一个值，但是其他条件下就不一定了

# def power1(x,n):
#     s=1
#     while n>1:
#         n=(n+1)-1
#         s=s*x
#     return s
# c=power1(5,3)
# print(c) #power1 中的 n 无法递减，因而导致无限循环。如果运行该函数，程序将一直循环下去，永远不会返回结果。

#默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
a = power(5)#只有必选参数
b = power(5,3)#依旧可以同时写必选参数和默认参数
print(a)
print(b)


def enroll(name,gender,age=7,city='shanghai'):
    print('这个小朋友的名字:',name)
    print('性别是：',gender)
    print('城市是：',city)
    print('old:',age)
a=enroll('tlf','F')
print(a) # 由于函数没有返回值，因此会输出 None

def enrolls(name,gender,age=7,city='shanghai'):
    s=name,gender,age,city
    print('这个小朋友的名字:',name)
    print('性别是：',gender)
    print('城市是：',city)
    print('old:',age)
    return s
b=enrolls('tlf','F')
print(b)
# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：

# >>> enroll('Sarah', 'F')
# name: Sarah
# gender: F
# age: 6
# city: Beijing
# 只有与默认参数不符的学生才需要提供额外的信息：

# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，
# 意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

# 先定义一个函数，传入一个list，添加一个END再返回：
# def add_end(L=[]):
#     L.append('END')
#     return L
# 当你正常调用时，结果似乎不错：
# >>> add_end([1, 2, 3])
# [1, 2, 3, 'END']
# >>> add_end(['x', 'y', 'z'])
# ['x', 'y', 'z', 'END']
# 当你使用默认参数调用时，一开始结果也是对的：
# >>> add_end()
# ['END']
# 但是，再次调用add_end()时，结果就不对了：
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#  特别注意
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc([1,2,3,4]))
print(calc((1,2,3,4)))
#*numbers 表示这个函数可以接受任意数量的参数，所有传入的参数会被打包成一个元组 numbers。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3,4))
print(calc())
#def calc(*numbers): 可以接受任意数量的位置参数，自动打包成元组。
#def calc(numbers): 只能接受一个参数，且你需要保证传进去的是一个可迭代对象（列表、元组等）。

num = [1,2,4]
nums=(2,3,4)
print(calc(num[0],num[1],num[2]))
#这种写法当然是可行的，问题是太繁琐，
# 所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(*num)
print(num)
print(*nums)
print(nums)
print(calc(*num))
print(calc(*nums))

#*单星号 :
#  用于接收任意数量的位置参数，它会把这些参数打包成一个 tuple。
# **双星号 : 
# 用于接收任意数量的关键字参数，它会把这些参数打包成一个字典，字典中的键（key）是参数的名字，值（value）就是对应的值。
def person(name,age,**othermessage):
    print('name:',name,'age:',age,'other:',othermessage)
a=person('tlf',22)
b=person('tlf',22,Height=168.5,weight='58kg',city='ZhengZhou')
print(a)
print(b)
#默认返回 None：如果函数没有 return 语句，调用函数的返回值默认是 None。
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
c={'city':'zhengzhou','job':'Engineer'}
person('tlf',23,**c)

def person(name,age,**otherthing):
    if 'city' in otherthing:
        pass# 目前占位，没有执行操作
    if 'job' in otherthing:
        pass# 目前占位，没有执行操作
    print('name:',name,'age:',age,'other:',otherthing)
person('tlf',23,city='zhengzhou')

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person(name,age,*,city,job):
    print(name,age,city,job)
person('tlf',23,city='zhengzhou',job='Engineer')

def person(name,age,*,city='zhengzhou',job):
    print(name,age,city,job)
person('tlf',23,job='Engineer')

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def demo(a, b, c=3, *args, d, e=5, **kwargs):
    """
    参数说明：
    - a, b 是位置参数，调用时必须提供并且按顺序赋值。
    - c 是默认参数，如果调用时不传，默认值为3；如果通过位置传递，会被覆盖。
    - *args 接收额外的位置参数，存储为一个元组。
    - d, e 是命名关键字参数，必须以关键字形式传入，其中 e 有默认值5。
    - **kwargs 接收其他所有额外的关键字参数，存储为一个字典。
    """
    print("a:", a)                # 第1个位置参数
    print("b:", b)                # 第2个位置参数
    print("c:", c)                # 第3个位置参数或默认参数
    print("args:", args)          # 所有额外的位置参数
    print("d:", d)                # 命名关键字参数 d
    print("e:", e)                # 命名关键字参数 e（默认值为5）
    print("kwargs:", kwargs)      # 所有额外的关键字参数

# 调用 demo 函数

# 解释：
# 位置参数：1 给 a，2 给 b，第三个位置参数 99 给 c。
# *args 会收集剩余的位置参数 100 和 101，组成元组 (100, 101)。
# 命名关键字参数：d 必须使用关键字提供，这里传 d=4；e 如果给出则使用传入值，这里传 e=8。
# **kwargs 会收集剩余的关键字参数，例如 extra1 和 extra2。
demo(1, 2, 99, 100, 101, d=4, e=8, extra1="hello", extra2="world")

"""
a: 1
b: 2
c: 99
args: (100, 101)
d: 4
e: 8
kwargs: {'extra1': 'hello', 'extra2': 'world'}
"""

def mul(*numbers):
    """
    计算所有传入数字的乘积

    参数：
        *numbers：可变参数，传入任意数量的数字

    如果没有传入任何参数，则抛出 TypeError 异常
    """
    # 如果没有任何参数，主动抛出 TypeError 异常
    if len(numbers) == 0:
        raise TypeError("mul() missing at least one argument")
    
    product = 1
    # 遍历所有传入的数字，累乘
    for n in numbers:
        product *= n
    return product

# 测试代码

# 当只传入一个数字时，应返回这个数字本身
print('mul(5) =', mul(5))
# 传入两个数字：5*6 = 30
print('mul(5, 6) =', mul(5, 6))
# 传入三个数字：5*6*7 = 210
print('mul(5, 6, 7) =', mul(5, 6, 7))
# 传入四个数字：5*6*7*9 = 1890
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))

# 检查各个测试结果是否正确，依次判断
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        # 如果调用不传参数的 mul() 不抛异常，就说明测试失败
        mul()
        print('mul()测试失败!')
    except TypeError:
        # 正确的做法是当不传参数时抛出 TypeError 异常
        print('测试成功!')
