from max_min import finminandmax
if finminandmax([])!=[None,None]:  #[]列表返回的应为()元组，因为函数定义的为元组(min_val,max_val)
    print('error')
elif finminandmax([7])!=[7,7]:
    print('error')
elif finminandmax([1,3,4,8,12,-1])!=[-1,12]:
    print('error')
else:
    print('测试成功')


from max_min import finminandmax
if finminandmax([])!=(None,None):  
    print('error')
elif finminandmax([7])!=(7,7):
    print('error')
elif finminandmax([1,3,4,8,12,-1])!=(-1,12):
    print('error')
else:
    print('测试成功')

