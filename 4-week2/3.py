#filter()
def f(x):
    return x%2==1
result=filter(f,[1,2,3,4,5,6])
print(list(result))

def g(s):
    return s and s.strip()
result=list(filter(g,['A','','C','1']))
print(result)
#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#构造无限奇数序列
def f(n):
    return lambda x:x%n>0
#定义一个“筛除倍数”的函数
def primes():
    yield 2 # 先返回2，它是最小的素数
    it = _odd_iter() # 初始化一个奇数序列:3,5,7,9,....
    while True:#开始一个无限循环。这个生成器没有结束条件（除非你手动 break），因为素数是无限的。
        n=next(it)# 取出序列的第一个数,每次从当前“奇数序列”里取出第一个数 n
        yield n# 这个数就是素数
        it=filter(f(n),it)
for n in primes():
    if n < 100:
        print(n)
    else:
        break