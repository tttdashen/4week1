# while True:
#     print("这是一个死循环")

#ython内置了字典：dict的支持，dict全称dictionary，
#在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#字典为{}
d = {'a':100,'b':89,'c':70}
print(d['a'])

d['a']=1
print(d['a'])
d['a']=2
print(d['a'])
#如果key不存在，dict就会报错
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('a' in d)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('d'))
print(d.get('d','aaa'))
print(d.get('d',2))#2是常量或者'aaa'字符串格式

d = {'a':100,'b':89,'c':70}
d.pop('a')
print(d)
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

#所以，dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
# 需要牢记的第一条就是dict的key必须是不可变对象。key即为前面的'a'等
#要保证hash的正确性，作为key的对象就不能变。
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
#>>> key = [1, 2, 3]
# >>> d[key] = 'a list'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = {1,2,3}#直接创建集合，但注意如果写空集合时不能使用 {}（因为 {} 表示空字典），而应使用 set()。
print(s)
s=set()
print(s)
s=set([1,2,3])#这种方式是通过将列表 [1,2,3] 转换成集合，同样得到 {1, 2, 3}。
print(s)

s = {1, 1, 2, 2, 3, 3}
print(s)#重复元素在set中自动被过滤
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(3)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1={1,2,3}
s2={2,3,4}
print(s1&s2)
print(s1|s2)
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。



# 试试把list放入set，看看是否会报错   这句话怎么理解
# 在 Python 中，set（集合）的元素要求必须是可哈希（hashable）的，而 list 是一种可变类型，不可哈希。所以“试试把 list 放入 set，
# 看看是否会报错”这句话的意思是让你尝试将一个列表作为集合中的元素，从而验证是否会出现类型错误（TypeError）。
# 例如，下面这段代码会报错：
# # 尝试将列表作为集合的元素
# s = { [1, 2, 3] }
# print(s)
# 运行后会抛出错误：
# TypeError: unhashable type: 'list'
# 这是因为集合内部必须用不可变对象（如整数、字符串、元组等）作为元素，而列表是可变对象，所以不能放入集合中。

#str是不变对象，而list是可变对象。
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a=['c','b','a']
a.sort()
print(a)

b='abc'
print(b.replace('a', 'A'))
print(b)
#虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'
# 要始终牢记的是，b是变量，而'abc'才是字符串对象！
# 有些时候，我们经常说，对象b的内容是'abc'，但其实是指，b本身是一个变量，它指向的对象的内容才是'abc

#即使 tuple 本身是不可变的，但其内部的数据类型也会影响其能否作为字典键或集合元素。