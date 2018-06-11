# 给妹子讲python
# S01E19

# 1.python中独特的嵌套函数
# 2.嵌套作用域与闭包现象
# 3.nonlocal关键字与内嵌作用域变量修改

#--------------------------------------------------#

def f1():
	x = 88
	def f2():
		print(x)
	f2()

f1()

# 嵌套作用域在嵌套的函数返回后却仍然有效
# f1()退出接触但f2()仍然记住了f1潜逃作用域内的变量名x
# 闭包：能够读取其他函数内部变量的函数。
def f1():
	x = 88
	def f2():
		print(x)
	return f2

action = f1()
action()

# 工厂函数
# 这种嵌套作用域引用，就是python的函数能够保留状态信息的主要方法了。
def maker(n):
	k = 8
	def action(x):
		return x ** n + k
	return action

f = maker(2)
print(f)
print(f(4))

# 内嵌函数内部想对嵌套作用域中的变量进行修改，就要使用nonlocal进行声明。
def test(num):
	in_num = num
	def nested(label):
		nonlocal in_num
		in_num += 1
		print(label, in_num)
	return nested

# 多次调用工厂函数返回的不同内嵌函数副本F与f，彼此间的内嵌变量in_num是独立隔离的。
F = test(0)
F('A')
F('B')
f = test(0)
f('a')
f('b')
f('c')
F('c')

#--------------------------------------------------#