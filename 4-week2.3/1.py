#面向对象和面向过程的语言区别

'''
求班级成绩与
'''
#面向过程
students=[]#构建一个空列表
def add_student(name,score):
    students.append({'name':name,'score':score})
def average_score():
    total=0
    for s in students:
        total += s['score']
    return total/len(students)
def print_all():
    for s in students:
        print(f'姓名：{s['name']},成绩:{s['score']}')
add_student('tlf',79)
add_student('tanlongfei',60)
print_all()
print('平均分:',average_score())

#面向对象
# 面向对象的写法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print(f"姓名: {self.name}，成绩: {self.score}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_score(self):
        total = sum(s.score for s in self.students)
        return total / len(self.students)

    def print_all(self):
        for s in self.students:
            s.print_info()

# 使用流程
manager = StudentManager()
manager.add_student(Student('小明', 85))
manager.add_student(Student('小红', 90))
manager.print_all()
print("平均分:", manager.average_score())
print('_'*50+'\n')

#饭店点菜系统：记录点了什么菜，计算总价格
#面向过程

dishes=[]#创建空列表保存所有菜

def add_dish(name,price):#添加一个菜及其价格
    dishes.append({'name':name,'price':price})

def total_price():## 计算总价
    total = 0#初始为0
    for dish in dishes:
        total += dish['price']
    return total

def print_menu():# 打印菜单
    for dish in dishes:
        print(f'菜名：{dish['name']},价格:{dish['price']}元')

#实际使用
add_dish('宫保鸡丁',25)
add_dish('辣子鸡丁',30)
print_menu()#打印的数据是两行，每调用一次 print()，就自动换一行，你即使没有写 \n，它也会帮你加上换行。
print('总价:',total_price(),'元')    

#面向对象
#定义一个类:Dish,用来表示每一道菜
class Dish:#类 Dish 代表一个“菜”，每个菜有自己的 name 和 price，所以我们用 __init__ 方法把这些信息绑定到具体的对象上。
    def __init__(self,name,price):#每个class的定义都需要self
        self.name=name# # 把传进来的 name 保存成这个对象的属性
        self.price=price# # 把传进来的 price 保存成这个对象的属性
    def show(self):# 为什么不用传 name 和 price？
        # 🧠 设计原因：因为 name 和 price 已经保存在对象里面，不需要额外传
        print(f'菜名：{self.name},价格：{self.price}元')
#方法 show 是“对象自己的行为”，直接使用对象内部的属性，不需要外面再传

#定义一个类:Menu,用来表示整个菜单
class Menu:
    def __init__(self):#经典第一步__int__和加self
        self.dishes=[]#初始化一个空列表
    def add_dish(self,dish):
          # dish 是一个 Dish 对象，我们要把它加进菜单列表
        # 🧠 设计思想：菜单不关心“菜的内容”，只需要接收一个 Dish 对象
        self.dishes.append(dish)
    def total_price(self):
        # 这里不传 price，因为 self.dishes 里面已经有所有菜了
        # 🧠 设计思想：这个类自己知道有哪些菜（已经保存在 self.dishes）
        return sum(dish.price for dish in self.dishes)
    def show_all(self):
        for dish in self.dishes:
            dish.show()# 调用每个 Dish 对象自己的 show() 方法

menu=Menu()  # 创建一个菜单对象，里面是空的
# 添加两个 Dish 对象
menu.add_dish(Dish("宫保鸡丁", 25))  # 这里 Dish 是创建菜，add_dish 是加入菜单
menu.add_dish(Dish("鱼香肉丝", 22))
menu.show_all()
print('总价:',menu.total_price(),'元')