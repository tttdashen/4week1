# pass 语句在 Python 中看似什么都不做，但它有非常实用的作用。主要用途有以下两点：

# 占位符
# 当你在编写代码时，还没有确定具体的实现逻辑，可以先写一个函数、类或循环的结构，填入 pass 作为占位符。这样既保证了代码语法的正确性，也能让整个程序顺利运行，之后再补充具体实现。

# 保持语法结构完整
# 某些场合 Python 语法要求必须有语句，而你又不打算写任何内容。这时用 pass 来“充数”，以防止语法错误。

def pop():
    pass#空函数
pop()#这种情况下，pop() 函数什么都不做，但编写者可以在将来再填充具体实现。


#假设你正在设计一个程序的总体结构，但具体实现尚未完成。你可以先写出框架，然后使用 pass 占位：

def initialize():
    # 初始化一些环境参数
    pass  # TODO: 后续实现初始化逻辑

def process_data(data):
    # 对数据进行处理
    pass  # 待实现数据处理过程

def cleanup():
    # 清理资源
    pass  # 清理操作待补充

def main():
    initialize()
    sample_data = [1, 2, 3]
    process_data(sample_data)
    cleanup()

if __name__ == '__main__':
    main()



#参数检查
from my_abs import my_abs
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
#print(my_abs(1,2))

#但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：

# my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in my_abs
# TypeError: unorderable types: str() >= int()
# >>> abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，
# 而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# if not isinstance(x, (int, float)):
#     raise TypeError('bad operand type')
# isinstance(x, (int, float)) 判断 x 是否属于 int 或 float 类型。

# 如果 x 不是这两种类型之一，not 会使得条件成立，从而执行 raise TypeError('bad operand type') 语句。

# raise 用来主动抛出异常，告诉调用者传入了不符合要求的参数类型。这种做法有助于及早发现错误，防止错误数据继续传播。

