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