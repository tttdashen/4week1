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

#break用法
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
#打印1-100
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue
n = 0
while n < 10:
    n = n + 1
    print(n)
#上面的程序可以打印出1～10
#但是，如果我们想只打印奇数，可以用continue语句跳过某些循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#break语句可以在循环过程中直接退出循环
#而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句
# 上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。