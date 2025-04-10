def power(x,n):
    s = 1
    while n>0:
        n= n-1
        s= s*x
    return s

a=power(5,3)
print(a)

# def powers(x,n):
#     s=x
#     while n>0:
#         n=n-2
#         s = x*s
#     return s
# b=powers(5,3)
# print(b)
#错误的，虽然5，3条件下和函数1为同一个值，但是其他条件下就不一定了
def power1(x,n):
    s=1
    while n>1:
        n=(n+1)-1
        s=s*x
    return s
c=power1(5,3)
print(c) #power1 中的 n 无法递减，因而导致无限循环。如果运行该函数，程序将一直循环下去，永远不会返回结果。

