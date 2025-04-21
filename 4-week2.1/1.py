#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#*args可以接收 任意多个位置参数，打包成一个元组（tuple）
#当你不知道用户会传几个参数的时候，就可以用 *args。
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax +n
    return ax
#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax# 这个 return 是返回计算结果
    return sum#这个 return 是返回函数本身
f=lazy_sum(1,2,4,7)## f 是一个函数，还没执行
print(f)#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(f())# # 调用 f() 才会真正计算 1 + 2 + 4 + 7 = 14
'''
return ax 是说：
“我已经算完总和了，把它的值返回出去”
比如：1 + 2 + 3 = 6
return sum 是说：
“我没有直接给你结果，我给你一个【函数】，你可以以后自己调用这个函数来得到结果”
'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#所以不用想那么多，你看f1, f2, f3 = count()直接就是调用range（1，4）里面的前三位：1，2，3 
#只不过在def f():return i*i里只取最后一位变量，也就3，所以都反回的就是3 3 3也就是9 9 9，
# 即原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

#解决方法：
#如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def g(j):
        def f():
            return j*j
        return f
    gs = []
    for i in range(1,4):
        gs.append(g(i))
    return gs
g1, g2, g3 = count()
print(g1(),g2(),g3())
'''
前者函数是把函数 f 放进了列表，但 f 里引用的是外部变量 i，这个 i 是共享的、唯一的变量”。
后者函数是g(i) 是立刻执行的函数，它会创建一个内部函数 f()，并且将当前的 i 作为 j 固定住（通过参数传值）

即：✅ 第一种是：先把函数放进列表，但它们内部引用的是共享变量 i，所以等到执行时，i 已经是 3 了。

✅ 第二种是：用函数把当前 i 的值传进来“锁定”到新变量 j 上，每个函数都保存了独立的 j，所以能得到正确的结果。
'''

#使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inx():
    x=0
    def inx_1():
        return x+1
    return inx_1
f=inx()
print(f())
print(f())
print(f())

'''
def inc():
    x = 0
    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2
#但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
'''
#原因是x作为局部变量并没有初始化，直接计算x+1是不行的。但我们其实是想引用inc()函数内部的x，所以需要在fn()函数内部加一个nonlocal x的声明。
#加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2


def createCounter():
    count=0
    def counter():
        nonlocal count
        count=count+1#count += 1
        return count
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#一个函数可以返回一个计算结果，也可以返回一个函数。

#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。