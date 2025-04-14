#迭代
dict = {'a':1,'b':2,'c':3,'aa':4}#dict是迭代对象
for key in dict:
    print(key)

"""
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
"""
for value in dict.values():
    print(value)

for k,v in dict.items():
    print(k,v)

a = 'ABC'#字符串也是迭代对象
for ch in a:
    print(ch)
for x in 'XYZ':
    print(x)

#所以，当我们使用for循环时
# 只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：
from collections.abc import Iterable#调用函数
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))

#如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,2),(2,4),(3,9)]:
    print(x,y)

def finminandmax(L):
    if len(L)==0:
        return(None,None)
    min_val=L[0]
    max_val=L[0]
    for x in L:
        if x<min_val:
            min_val = x
        if x>max_val:
            max_val = x
    return(min_val,max_val)
