'''
模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

创建自己的模块时，要注意：

模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
'''

#!/usr/bin/env python3     可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf8 -*-     表示.py文件本身使用标准UTF-8编码；
'a test module'            #表示模块的文档注释
__author__='tlf'           #作者名

#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
import sys #导入模块

def test():
    args=sys.argv     
    if len(args) == 1:         # 只有脚本名
        print('Hello, world!')
    elif len(args) == 2:       # 额外传了一个名字
        print('Hello, %s!' % args[1])#%s 是一个 占位符，意思是“这里要填一个字符串”  
#   % args[1] 是告诉 Python：“请把 args[1] 放到 %s 这里去”
    else:
        print('Too many arguments!')
#sys.argv 永远至少有 1 个元素：
#根据列表长度判断用户是否传入名字


if __name__ == '__main__':
    test()





'''
Python 脚本的“入口判断语句”，作用非常大！
每个 Python 文件运行时，解释器会给它自动设置一个变量：__name__

如果你是 直接运行这个文件，比如：
python hello.py
此时：
__name__ == '__main__'   ✅ 成立
但如果你是 import 它作为模块，例如：
import hello
__name__ == 'hello'      ❌ 不等于 '__main__'
✅ 所以这句的作用：
✔ 表示：只有当你直接运行这个文件时才会调用 test()
✔ 如果你只是导入它，就不会自动执行 test()，而是要手动写：
'''
