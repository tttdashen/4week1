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
print('_'*30)

#如果装饰器本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(fnc):
        def wrapper(*args,**kw):
            print(f'[{text}] call:',fnc.__name__)
            return fnc(*args,**kw)
        return wrapper
    return decorator
#手动替换
@log('Debug')
def today():
    print("2024-6-1")
today()
print('_'*30)

#问题：装饰后，today.__name__ 变成 wrapper，元信息丢失。
#解决：在 wrapper 上加 @wraps(func)
from functools import wraps

def log(text):
    def decorator(func):
        @wraps(func)                 # ← 关键：一行搞定元信息复制
        def wrapper(*a, **k):
            print(f"[{text}] call", func.__name__)
            return func(*a, **k)
        return wrapper
    return decorator
@log("INFO")
def today():
    """Print today."""
    print("2024-6-1")

today()
print("函数名  :", today.__name__)   # 仍然是 today
print("文档字符串:", today.__doc__)  # 仍然存在
print('_'*30)





import time
import functools
'''
import time | 引入标准库 time，里面有 高精度计时 函数
import functools | 引入 functools.wraps，用于保留原函数元数据
'''

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**hw):
        start = time.perf_counter()
        result=fn(*args,**hw)
        end=time.perf_counter()
        cost_ms=(end-start)*1000
        print(f'{fn.__name__} exxcuted in {cost_ms:.3f}')
        return result
    return wrapper
'''
装饰器函数 metric(fn)
def metric(fn): | 第 1 层函数：接收 被装饰 的函数对象 fn
@functools.wraps(fn) | 给下一层 wrapper 打补丁，让它保留 fn.__name__、fn.__doc__ 等属性
def wrapper(*args, **kwargs): | 第 2 层函数：真正执行“计时 + 调用 + 打印”逻辑；*args, **hw 使其兼容任何参数形式

2.1 计时三步
start = time.perf_counter() | 记录高精度起点 | perf_counter() 专为性能计时设计，比 time.time() 精度更高
result = fn(*args, **kwargs) | 真正调用原函数 | 参数原样转发，确保不破坏调用方式
end = time.perf_counter() | 记录高精度终点 | 与起点相同 API，保证精度一致

2.2 结果处理
(end - start) 得到 秒，乘 1000 转为 毫秒
:.3f 格式化：保留 3 位小数
fn.__name__ 打印原函数名称，得益于 @wraps(fn) 保留

2.3 返回值
return result
装饰器的 wrapper 必须把原函数的返回值传回调用者，否则功能被破坏

2.4 返回“新函数”
return wrapper
metric(fn) 的最终返回值 不是结果，而是新函数
解释器看到 @metric 时，会把 fast = metric(fast) 绑定过去

'''




@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

'''
3. 使用装饰器的两种写法
@metric | fast = metric(fast)
@metric（带参数的情况） | 若要写 @metric("DEBUG")，就需要 3 层函数，原理同前面讲过
'''


f=fast(11,22)
s=slow(11,22,33)

print("fast return ->", f)
print("slow return ->", s)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试通过!')

#这段 @metric 代码到底干了什么？
# 一句话：
# 给任何函数贴上 @metric，它就会在每次调用时自动告诉你——
# “这个函数从开始到结束，一共花了 X 毫秒”。

