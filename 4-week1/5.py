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
list = []
print(len(list))