#面向对象和面向过程的语言区别

'''
求班级成绩与平均成绩
'''


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

'''
饭店点菜系统
'''
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
print('_'*30)


'''
图书馆借书系统：
共两个类

定义书：
1.书的信息-名字-作者-初始状态
2.书籍的基本状态-是否可以借
3.借还书的逻辑：
（1）书未被借：借书打印借书成功的信息---书背借了：打印借书失败的信息
（2）书没有被借：打印书本来就没被借出去何谈归还---书被借走了：打印成功归还

定义图书馆：
1.定义图书馆：用于保存所有书
2.图书馆添加书籍功能
3.图书馆打印目前所有藏书信息
4.图书馆借书功能--是否可以借书
5.图书馆遍历功能-可以确定借的书是否在藏书中

实际操作：
1.创建图书馆对象
2.添加书籍给图书馆-图书馆类功能
3.查看所有书籍功能-图书馆类功能
4.借出某本书-图书馆类功能
5.再借一次试试看-图书馆类功能
6.归还-图书馆类功能
7.查看图书馆藏书状态变化-图书馆类功能
'''
class Book:
    def __init__(self,title,author):
        self.title= title
        self.author = author
        self.is_borrowed=False # 初始状态是未借出
    def display_info(self):
        status = '已借出' if self.is_borrowed else '可借'
        print(f'{self.title} by {self.author} - 状态：{status}')
    def borrow(self):
        if self.is_borrowed:
            print(f"{self.title} 已经被借出去了")
        else:
            self.is_borrowed = True
            print(f'你已经成功借阅了 {self.title}')
    def return_book(self):
        if not self.is_borrowed:
             print(f"{self.title}本来就没有被借出")
        else:
             self.is_borrowed = False
             print(f"你已成功归还《{self.title}》")


'''
等同于
if self.is_borrowed:
    status='已借出'
else:
    status='可借'

self.is_borrowed=False # 初始状态是未借出
但是if self.is_borrowed: 这句的意思其实是：
✅ “如果这个书的 is_borrowed 是 True（即已经被借出）
''' 

class Library:
    def __init__(self):
        self.books=[]# 用于保存所有 Book 对象
    def add_book(self,book):
        self.books.append(book)
        print(f"已添加书籍：《{book.title}》")
    def list_books(self):
        print("当前图书馆藏书：")
        for book in self.books:
            book.display_info()
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"没有找到《{title}》这本书")
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"没有找到《{title}》这本书")

# 创建图书馆对象
lib = Library()

# 添加书籍
lib.add_book(Book("三体", "刘慈欣"))
lib.add_book(Book("活着", "余华"))

# 查看所有书籍
lib.list_books()

# 借出一本书
lib.borrow_book("三体")

# 再借一次试试看
lib.borrow_book("三体")

# 归还
lib.return_book("三体")

# 查看状态变化
lib.list_books()
print('_'*30)


#班级成绩管理系统
'''
两个类：
student：
1.学生信息：姓名-学号-成绩
2.属性：显示学生信息

classroom：
1.属性：保存所有学生
2.方法：
添加学生-显示所有学生信息-计算所有学生平均分-查找指定学号学生信息

实际操作：
1.创建班级对象
2.添加学生信息
3.打印学生列表
4.打印全班平均分
5.查找某个学生成绩
'''
class Student:
    def __init__(self,name,number,score):
        self.name=name
        self.number=number
        self.score=score
    def display_info(self):
        print(f'姓名:{self.name},学号：{self.number},成绩：{self.score}')

class Classroom:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
        print(f'添加成功：{student.name}')
    def list_students(self):
        print('全班学生信息：')
        for student in self.students:
            student.display_info()
    def average_score(self):
        if not self.students:
            print('暂无学生信息')
            return
        total = sum(s.score for s in self.students)
        avg = total/len(self.students)
        print(f"全班平均分：{avg:.2f}")
    def find_student(self,student_number):
        for s in self.students:
            if s.number == student_number:
                print('查找结果为：')
                s.display_info()
                return
        print(f"未找到学号为 {student_number} 的学生")

classroom=Classroom()
classroom.add_student(Student("小明", "202301", 85))
classroom.add_student(Student("小红", "202302", 92))
classroom.add_student(Student("小刚", "202303", 76))
classroom.list_students()
classroom.average_score()
classroom.find_student("202302")
classroom.find_student("202399")