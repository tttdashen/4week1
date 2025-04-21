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

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L,key=by_name)
print(L2)
def by_point(s):
    return s[1]
L3 = sorted(L,key=by_point)
print(L3)