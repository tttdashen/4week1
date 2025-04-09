names = ['a','b','c']
for name in names:
    print(name)

sum = 0
for x in[0,1,2,3,4,5]:
    sum =sum+x
print(sum)

#如何计算1..1000的和呢
print(list(range(5)))

sum = 0
for x in range(101):
    sum=sum+x
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n>0:
    sum = sum + n
    n=n-2
print(sum)

names = ['a','b','c']
for name in names:
    print(f'Hello,{name}!')
