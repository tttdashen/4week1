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
