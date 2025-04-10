def a_and_b(x,y):
    chu = x//y # 计算整数商（向下取整的除法）
    yu = x%y# 计算余数
    return chu,yu
q,r=a_and_b(18,7)
print('商是：',q)
print('余是：',r)
r = a_and_b(18,7)
print('完成的结果：',r)

import math
def quadratic(a,b,c):
    z=b**2-4*a*c
    x1=(-b+math.sqrt(z))/2*a#调用平方根函数sqrt需要加上调用的总模块math
    x2=(-b-math.sqrt(z))/2*a
    return x1,x2
a,b=quadratic(1,0,-1)
print('第一个解x为：',a)
print('第二个解x为：',b)

#上述这个很完善，但是没有考虑一元二次方程a为0等情况
import math
def quadratic(a,b,c):
    if a==0:
        raise ValueError('参数a不能为0，为0不算二元一次方程')
    if a<0:
        raise ValueError('方程没有实数根')
    z=b**2-4*a*c
    x1=(-b+math.sqrt(z))/2*a#调用平方根函数sqrt需要加上调用的总模块math
    x2=(-b-math.sqrt(z))/2*a
    return x1,x2


a,b=quadratic(1,0,-1)
print('第一个解x为：',a)
print('第二个解x为：',b)
print('根为：',a,b)

a,b=quadratic(-1,2,2)
print('根为：',a,b)