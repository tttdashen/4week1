#map函数的讲解
#
#
def f(x):
    return x**2
A=[1,2,3,4,5]
result=map(f,A)#map函数的用法，map(函数, 可迭代对象)
print(list(result))

#lambda (匿名函数)语法简写：
A=[1,2,3,4,5]
results=map(lambda x:x**2,A)
print(list(results))
A=[1,2,3,4,5]
results=map(lambda x:x**2,A)
print(list(results))


#eg2:
words=['abc','xyz','tlf']
Capotalize_words=map(str.upper,words)#str.upper是py内置的大写函数，所以不用用lambda定义
print(list(Capotalize_words))

#eg3：map 其实也可以“同时遍历多个列表”！
a=[1,2,3,4]
b=[4,5,6]
result=map(lambda x,y:x*y,a,b)
print(list(result))

#eg4：与for对比
nums=[1,2,3]
nex_nums=[]
for n in nums:
    nex_nums.append(n**2)
print(nex_nums)
# 用 map 实现
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6]
#map() 是 函数式编程风格，相比 for 循环：更加“简洁”更利于链式处理

A = [1,2,3,4,5,6,7]
result=map(str,A)
print(list(result))
#全部转化为字符串

#reduce用法
'''''
reduce() 函数格式
from functools import reduce  # 需要先导入
reduce(函数, 序列)
它的工作方式：
假设序列为：[x1, x2, x3, x4]
步骤如下：
step1: 先计算 f(x1, x2) → 得到r1
step2: 再计算 f(r1, x3) → 得到r2
step3: 再计算 f(r2, x4) → 得到r3
...
最终结果就是 reduce 的输出
'''''
from functools import reduce
def f(x,y):
    return x*y
nums=[1,2,3,4]
result=reduce(f,nums)
print(result)

from functools import reduce
result=reduce(lambda x,y:x*y,[1,2,3,4])
print(result)

from functools import reduce
nums=[1,2,3,4]
result=reduce(lambda x,y:x*10+y,nums)
print(result)

'''
和 map 的区别对比
功能	map	reduce
输入	函数 + 可迭代对象	函数 + 可迭代对象
输出	一个新的迭代器（多项）	一个最终结果（单项）
应用场景	每个元素转换	元素累计合并成一个值
'''
from functools import reduce
DIGITS={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def d(s):
    def f(x,y):
        return x*10+y
    def g(ch):
        return DIGITS[ch]
    return reduce(f,map(g,s))
print(d('123456'))
#这个就是int函数的用法

from functools import reduce
DIGITS={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def g(ch):
    return DIGITS[ch]
def d(s):
    return reduce(lambda x,y:x*10+y,map(g,s))
print(d('12345678'))


