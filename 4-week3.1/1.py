#错误处理
#📚 1. 为什么要有 try...except
'''
原始做法（错误码）
def foo():
    r = some_function()
    if r == -1:
        return -1
    return r

正常值和错误码混在一起，区分麻烦。
错误要一层一层传递上去，很繁琐。'''

#更好的做法（异常处理）
#用 try...except...finally：
#📚 2. try-except-finally 基本用法
'''
try:
    # 可能出错的代码
except 错误类型:
    # 出错的处理逻辑
finally:
    # 无论对错，都会执行
'''
from typing import final


try:
    r =10/0
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally...')
#✅ 错误发生后，except捕获；finally无论如何都会执行。

#3. 多个 except 和 else
try:
    r=10/int('a')
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('no Error!')
finally:
    print('finally...')

#📚 4. 错误继承关系要注意
# except ValueError:
#     ...
# except UnicodeError:
#     ...
'''
UnicodeError 是 ValueError 的子类

所以上面顺序下，UnicodeError 根本不会被匹配到

要小心继承关系，先捕子类，后捕父类

'''

#错误可以跨层捕获（不需要每一层都 try）

