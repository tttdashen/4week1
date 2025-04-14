L =list(range(100))
print(L)
print(L[0:10])
print(L[-10:])
print(L[:10:2])
print(L[::5])
print(L[:])
M=(1,2,3,4,5)
print(M[:2])
N = ['1','2','3']
print(N[0:2])
#切片操作

def trim(s):
    # 找到首个非空白字符的索引
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    # 找到末尾非空白字符的索引
    end = len(s) - 1
    while end >= start and s[end] == ' ':
        end -= 1
    
    # 使用切片返回去除两端空格后的字符串
    return s[start:end+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
