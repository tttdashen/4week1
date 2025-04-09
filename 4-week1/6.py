age = 15
if age >= 18:
    print('Your age is',age)
    print('adult')
else:
    print('Your age is',age)
    print('teeneger')

age = 5
if age>=18:
    print('Your age is,Your are adlut',age)
elif age>=6:
    print('Your age is,Your are teeneger',age)
else:
    print('Your age is,Your are kid',age)

#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
#此时判断的的是teenager

#if判断条件还可以简写，比如写：
#如果 x 为非零数值、非空字符串、非空列表、非空字典等，这些对象在布尔上下文中都被认为是 True。
x = 0
if x:
    print('True')
else:
    print('False')

x = "hello"
if x:
    print('True')

# birth=input('birth:')
# if birth >=2000:
#     print('你是00后')
# else:
#     print('你不是00后')
#输入数值报错，这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
#py提供了int()来转换为整数

a=input('birth:')
birth=int(a)
if birth>=2000:
    print('你是00后')
else:   #!!!!else分支不能跟任何条件
    prin('你不是00后')

name = 'tlf'
weight = '58kg'
height = '1.685m'#这些都是字符串，如果计算需要转换为数值或者直接weight = 58等
height_cm = 168.5
weight = float(weight.rstrip('kg'))     # 得到 58.0
height = float(height.rstrip('cm'))
bmi =weight/(height**2)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<32:
    print('肥胖')
else:
    print('过度肥胖')



#改良版
age = int(input("请输入你的年龄："))
if age >= 18:
    print("成年人")
else:
    print("未成年人")
weight = input("请输入你的体重（kg）：")
height_cm = input("请输入你的身高（cm）：")
# 将身高转换为米
height = height_cm / 100
# 计算 BMI，公式：BMI = 体重 / (身高 ** 2)
bmi = weight / (height ** 2)
print("你的 BMI 值为：", bmi)
# 根据 BMI 值判断体型
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:  # bmi >= 32 的情况
    print("过度肥胖")

