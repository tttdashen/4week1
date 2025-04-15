L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
for n in g:
    print(n)
#我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
"""
著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
"""
#斐波那契数列的基本实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6)

#Generator 函数：从函数到迭代器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#yield 关键字
##当函数执行到 yield 时，它会“产出”一个值，
##同时暂停函数执行，下次通过 next() 调用时，从暂停的地方继续执行，而不是从头开始。这种机制使得函数变成了一个generator。
f = fib(6)
print(f)  # 输出类似：<generator object fib at 0x...>
#普通函数是一次性执行到底，遇到 return 后函数结束；
# 而 generator 函数则会在每次遇到 yield 时返回当前值，并记录当前执行的位置，等待下一次恢复。
"""""
函数与 generator 的区别

普通函数一次性执行到底，遇到 return 后返回且结束。

包含 yield 的函数成为 generator 函数，每次调用 next() 都会中断并在下次继续执行。

代码简洁与内存效率
Generator 在处理大量数据或无限序列（如无穷斐波那契数列）时非常有用，因为它只在需要时生成下一个值，节省内存资源。

实际编程场景
在需要按需生成序列或数据流，而不是全部生成后占用内存时，推荐使用 generator。
"""""