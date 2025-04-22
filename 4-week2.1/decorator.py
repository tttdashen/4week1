# #函数也是对象,任何能被变量引用、能传参、能作为返回值的东西，都是 Python 一等公民（对象）。函数也是。
# def now():
#     print('My name is tlf')
# f=now
# f()#调用函数，等同于now()

# #_name_,函数的身份证
# #每个函数对象都有很多“内置属性”。
# #__name__ 就是“这个函数原来叫什么名字”。
# print(now.__name__)
# print(f.__name__)

# #装饰器（decorator）动机
# #需求：在 不改动原函数代码 的前提下，“偷偷”给函数加新功能。
# #举例：给 now() 自动打日志 ➜ “调用前说一声，调用后再说一声”。

'''
场景：给 now() 套一层“礼物包装”

def now():
    print("2024‑6‑1")
目标：在不改 now() 本身的前提下，让它执行前后自动打印日志
输出效果应类似：


[LOG] call now()
2024‑6‑1
[LOG] end  now()
Step 1 ― 写一个“包装工厂” log(func)

def log(func):                 # log 只接受 1 个参数：被包装的函数
    def wrapper(*args, **kwargs):
        print(f"[LOG] call {func.__name__}()")  # 前置日志
        result = func(*args, **kwargs)          # 关键：真正调用原函数
        print(f"[LOG] end  {func.__name__}()\n")# 后置日志
        return result                           # 别忘了把结果传回去
    return wrapper            # ← 关键！返回“新函数”而不是结果
log 做了两件事

接收 func（原函数）作为参数

返回 一个新函数 wrapper

——这就满足了“高阶函数 & 返回函数”两个条件。

Step 2 ― 【手动】把 now 换成 wrapper

now = log(now)    # 等价于：now = wrapper
                  # 此刻 now 指向的是“包装后”的函数
now()             # ← 真正调用
调用顺序示意图

now()  ─┬─► wrapper()   （先打印前置日志）
        │      │
        │      └─► func() = 原来的 now()  （输出 2024‑6‑1）
        │
        └─► wrapper()   （再打印后置日志）
输出结果：

[LOG] call now()
2024‑6‑1
[LOG] end  now()
Step 3 ― 用 @语法糖让“换函数”自动完成
@log          # 语法糖：解释器在定义完 now 后自动执行 now = log(now)
def now():
    print("2024‑6‑1")
看到 @log，就等价于刚才那句 now = log(now)

以后直接写 now() 就已经是“带包装”的版本

问题 | 一句话答案
log 为什么要再定义 wrapper？ | 因为我们想加“前后日志”又要继续调用原函数，只能包一层新函数。
wrapper 里 *args, **kwargs 干什么？ | 让包装器兼容任何参数形式（可传可不传）。
为什么要 return wrapper 而不是 return result？ | 我们要的是“新的、可重复调用的函数本体”，而不是一次性的调用结果。
log 返回的 wrapper 会不会丢失函数名？ | 默认会，把 wrapper.__name__ 变成 wrapper；用 from functools import wraps + @wraps(func) 可保留元信息。
记忆口令
装饰器 = (接收 函数) + (返回 函数)
@装饰器名 → 自动 new_func = 装饰器(old_func)

只要把它想成“给函数套礼物包装”，先送进去、再拿出来的就是“原礼物+包装”，就不会混淆了！
'''


#1.函数也是变量-可以赋值给变量
def now():
    print('I am tlf')
f=now
f()
print('now._name_:',now.__name__)
print('f._name_:',f.__name__)
print('_'*30)

#2.写一个打印日志的装饰器，不改变原函数的定义
def log(fnc):
    def wrapper(*args,**kwargs):
        print(f'[log] call {fnc.__name__}()')
        result=fnc(*args,**kwargs)
        print(f'[log] end {fnc.__name__}()')
        return result
    return wrapper

#3.用两种方式把 now()“打包”成带日志的新函数
#3-A手动替换
now_with_log=log(now)
print('手动调用 now_with_log():')
now_with_log()
print('_'*30)
#3-B使用@log语法糖
@log#等价于now=log(now)
def now():
    print('I am tlf')
print('再次调用now():')
now()

