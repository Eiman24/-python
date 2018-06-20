# 给妹子讲python
# S01E24

# 1.try、except、else、finally、raise关键字
# 2.异常的处理流程
# 3.try/except/else/finally组成的几种异常处理模式

#--------------------------------------------------#

# try:
#     main-action
# except Exception1:
#     handler1
# except Exception2:
#     handler2
# ...
# else:
#     else-block
# finally:
#     finally-block

# 就像往常一样，这个语句中的main-action代码会先执行。如果该程序代码引发异常，
# 那么所有except代码块就会逐一测试，寻找与抛出的异常相符的语句，如果引发的异常是Exception1，
# 就会执行handler1，如果引发的的异常是Exception2，就会执行handler2，以此类推，
# 如果没有引发任何异常，会执行else-block。而无论之前发生了什么，当main-action代码块完成的时候，
# 而任何引发的异常都已经处理后，finally-block就会执行。事实上，
# 即使异常处理器或者else-block内有错误发生而引发新的异常，finally-block内的程序代码依然会执行。
# 就像之前所说的那样，finally子句并没有终止异常：当finally-block执行的时候，如果异常还存在，
# 就会在finally-block代码块执行后继续传递，而控制权会跳至程序其他地方，如我们的默认的顶层处理器。


def fetcher(obj, index):
	return obj[index]

x = 'spam'

try:
	fetcher(x, 9)

except IndexError as e:
    print(e.args)

#--------------------------------------------------#