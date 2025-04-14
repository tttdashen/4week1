#range(n)会生成一个从0到n-1的整数序列，当n=4，生成0，1，2，3
#len(num)返回列表的长度
#range(len(num))可以生成一个num的整数序列
nums=[2,7,11,15]
found = False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==9:
            print(nums[i],nums[j])
            found = True
if not found:
    print('没有符合要求的数')
#最终结果返回2 7

#返回数组的下标
#.format() 方法是一种格式化字符串的方法，可以把预留的占位符 {} 替换为实际的变量值。
nums=[2,7,11,15]
target = 9
found = False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print('nums[{}]={}和nums[{}]={}的和为{}'.format(i,nums[i],j,nums[j],target))
            found = True
if not found:
    print('没有符合要求的数')
#nums[0]=2和nums[1]=7的和为9 

#力扣风格
