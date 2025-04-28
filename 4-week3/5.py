#1.动态创建类：type()
#普通写法：
class Hello(object):
    def hello(self,name='world'):
        print(f'Hello,{name}')
# 用 type() 动态创建 Hello 类：
def fn(self,name='world'):
    print(f'Hello {name}')
Hello = type('Hello',(object,),{'hello':fn})
#效果跟普通写法一模一样。

#type() 动态创建类，metaclass 动态修改类，ORM是 metaclass 的实际应用。