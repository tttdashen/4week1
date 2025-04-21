A=[5,4,2,7,10,'a']
only_numbers=[x for x in A if isinstance(x,int)]#sorted只能对纯数字的列表进行排序
print(sorted(only_numbers))

B=[2,7,-10,88,-100]
print(sorted(B,key=abs))#比较绝对值的大小

C=['bob', 'about', 'Zoo', 'Credit']
print(sorted(C))#对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
#['Credit', 'Zoo', 'about', 'bob']
print(sorted(C,key=str.lower))
print(sorted(C,key=str.lower,reverse=True))