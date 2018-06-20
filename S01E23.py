# 给妹子讲python
# S01E23

# 1.异常的默认处理和主动捕获
# 2.主动触发异常和自定义异常
# 3.finally终止代码块的用法

#--------------------------------------------------#

# 把调用封装在try语句内，自行捕捉异常。
def fetcher(obj, index):
	return obj[index]

x = 'spam'

try:
	fetcher(x, 9)
except IndexError:
	print('got exception')
print('continue...')

# 通过raise触发的异常的捕捉方式和python程序自身引发的异常一样
try:
	raise IndexError
except IndexError:
	print('got exception')

# 自定义的异常能够通过类来编写，它继承自一个内置的异常类：
# 通常这个类的名称叫做Exception
class Bad(Exception):
	pass
def doomed():
	raise Bad()

try:
	doomed()
except Bad:
	print('got Bad')

# try语句可以包含finally代码块。可以定义一定会在最后执行时的收尾行为。
try:
    raise IndexError
finally:
    print('in finally')
print('after finally')

try:
    print('ok')
finally:
    print('in finally')
print('after finally')

















#--------------------------------------------------#