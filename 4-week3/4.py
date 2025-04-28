'''
当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
好处是简单，缺点是类型是int，并且仍然是变量。

于是就想：
有没有一种方式，让：

每个月份是独立的、受保护的、不可随便乱改的常量？

并且它们是统一归类的，属于一个共同的类型？

✅ 答案就是 —— 用 Enum（枚举类型）！'''

from enum import Enum, unique
Month=Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
print(Month.Jan.value)

#📚 3. 如何枚举所有成员？
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#📚 4. 更复杂一点：自己定义 Enum 类
from enum import Enum
@unique
class Weekday(Enum):
    sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    #@unique 装饰器作用是：检查所有的 value 不能重复

    '''
    如果你不小心写成：

python
复制
编辑
Mon = 0
就会在程序运行时直接报错！

✅ 大大提高了程序安全性！

'''

'''
小总结：Enum到底解决了什么？

之前	用Enum以后	好处
普通变量，容易误改	枚举成员，受保护	程序更健壮
不统一，容易混乱	类型统一归属（Month/Weekday）	代码更规范
无检查机制	@unique 强制值唯一	避免逻辑错误
没有结构	有明确结构（成员名、成员值）	维护方便'''