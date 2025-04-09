print(ord('A'))
print(ord('中'))
print(ord('谭'))
print(chr(66))
print(chr(25991))

#使用 %d 占位符来格式化整数,使用 %f 占位符来格式化浮点数，可以指定小数点后的位数,使用 %s 占位符来格式化字符串。
# 可以指定输出的宽度，使输出对齐。例如 %10d 表示输出的整数至少占 10 个字符位置，右对齐； %-10s 表示输出的字符串至少占 10 个字符位
A = 1034
B = '数字为：%d'% A
print(B)
A = 10.445666
B = '数字为：%.2f'%A
print(B)
A = 'tlf'
B = 'Hello,%s!'%A
print(B)

age=22
Height = 166.588
name = 'tlf'
A = '我的年龄是：%d,我的身高是：%.1f,我的名字是：%s'%(age,Height,name)
print(A)

num = 42
s = "hello"
formatted_num = "数字：%10d" % num    # 右对齐，若不足10位前面填充空格
formatted_str = "字符串：%-10s" % s  # 左对齐，空位在右侧
print(formatted_num)  # 输出：数字：        42
print(formatted_str)  # 输出：字符串：hello     
