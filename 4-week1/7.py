#若利用if elif else判断的话会很长
#用match匹配

score = 'B'
match score:
    case 'A':
        print('score is A')
    case 'B':
        print('score is B')
    case 'C':
        print('score is C')
    case _:# _表示匹配到其他任何情况
        print('score is ???')

#复杂匹配
# match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

#匹配列表
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 解释：
# 匹配条件：列表中只有一个元素，且这个元素是字符串 'gcc'。
# 用途：当输入命令为 ['gcc'] 时，说明只输入了 gcc，没有跟随任何文件，所以打印错误提示：
# gcc: missing source file(s).
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#匹配条件：
# 这个分支要求列表的第一个元素是 'gcc'，第二个元素存入变量 file1，余下的任意元素（可以有也可以没有）收集到变量 files（*files 表示匹配多个剩余值）。
# 用途：
# 当命令列表以 'gcc' 开头，并且至少跟了一个文件时，会进入这个分支。
# 例如，对于列表 ['gcc', 'hello.c', 'world.c']，会将 'hello.c' 赋值给 file1，['world.c'] 赋值给 files。
# 程序随后拼接这些文件名打印出编译指令，例如：
# gcc compile: hello.c, world.c
    case ['clean']:
        print('clean')
# 匹配条件：列表中仅包含一个元素且等于 'clean'。
# 用途：如果用户输入命令 ['clean']，就会匹配这个分支，执行 print('clean')，输出提示或命令。
    case _:
        print('invalid command.')
