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



#将用户的首字母大写，其余小写

def normalize(name):
    return name.capitalize()
L1=['AbC','tlf','XYZ']
L2=list(map(normalize,L1))
print(L2)
'''
str.capitalize() 会将字符串变为：
第一个字母大写
其余全部小写
'''

def normalize(name):
    return name[0].upper()+name[1:].lower()
L1=['AbC','tlf','XYZ']
result=map(normalize,L1)
print(list(result))

#eg:2 实现累积
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*7*9=',prod([3,5,7,9]))
if prod([3,5,7,9])==945:
    print('测试成功')
else:
    print('测试失败')


#eg3 将字符串转化为浮点数
from functools import reduce
DIGITS={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def strfloat(s):
    int_part,frac_part=s.split('.')
    def f(x,y):
        return x*10+y
    def g(z):
        return DIGITS[z]
    int_value=reduce(f,map(g,int_part))
    frac_value=reduce(f,map(g,frac_part))/(10**len(frac_part))#原本得到的456应该除以1000，而1000=10**3，3是小数部分‘456’的长度
    return int_value+frac_value
print('strfloat(\'123.456\') =',strfloat('123.456'))
if abs(strfloat('123.456') - 123.456) < 0.00001:# < 0.00001的意义是避免浮点数精度误差！
    print('测试成功!')
else:
    print('测试失败!')

'''
浮点数在计算机中不是精确的
在 Python（和大多数编程语言）中：

浮点数是用 二进制近似 表示的

所以像 123.456 这种十进制小数，有时在内存中存储的其实是个“非常非常接近”的值，比如：

123.456  → 实际存的可能是 123.4559999999999998
所以不能用 == 比较浮点数
如果你写：

if str2float('123.456') == 123.456
它可能会 失败，因为：

str2float('123.456') → 123.455999999...
虽然人类看来是对的，但计算机会觉得“不等”。
解决办法：用误差范围来比较

abs(计算值 - 正确值) < 允许的误差
'''
