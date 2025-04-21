A=list(map(lambda x:x**x,[1,2,3,4,5]))
print(A)
'''
相当于
def f(x):
    return x*x
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f = lambda x:x**x
print(f)
print(f(2))
#同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y

L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)
