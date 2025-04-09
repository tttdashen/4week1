#列表list，初始化后可以增删改[]
name = ['a','b','c']
print(name)
print(name[0])
print(name[-1])
print(name[-2])
print(len(name))
# name = name.append('d'),这个是错误的
# name.append('d') 的作用：
# append() 是列表的一个方法，用来就地修改列表，在末尾添加一个元素。
# 它的返回值是 None。
# 所以，name = name.append('d') 的结果是把 None 赋值给 name，导致 name 不再是列表了，而是 NoneType。
name.append('d')
print(name[-1])
name.insert(0,'0')
print(name)
name.pop()
print(name)
name.pop(0)
print(name)
name[0] = 'd'
print(name)
list = ['a','1','True',['3','b'],'d']
print(len(list))
print(list[3][0])#层层嵌套
list = []
print(len(list))

#元组tuple，初始化后无法修改()
tuple = ('a','b','c')#()直观的就说出了是元组
print(tuple)
print(tuple[0])
t = ()
print(t)
#但是！！！！定义t=(1)有歧义，直接写 t = (1) 会产生误会。你可能认为这表示一个包含元素 1 的 tuple
#但实际上 Python 会把 (1) 当作数学表达式中的括号，只计算括号中的内容，结果是数字 1
t=(1)
print(t)#输出结果为1，如果是元组输出应该为(1)才对
t=(1,)
print(t)#正确写法，输出(1,)
#所以只有一个元素的元组，此时必须加,

#最后来看一个“可变的”tuple：
tuple = ('a','b',['c','d'],'e')
print(tuple[2][0])
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

#元组（tuple）,列表(list)内部的元素不强制要求都要用引号。是否加引号取决于你要存储的元素类型
#eg:
# t = (1, "hello", 3.14, True, [2, 3])