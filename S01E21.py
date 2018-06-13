# 给妹子讲python
# S01E21

# 1.基于位置和关键字的参数匹配
# 2.使用默认参数形式
# 3.函数定义使用*和**进行任意数目参数收集
# 4.函数调用时使用*和**进行参数解包

#--------------------------------------------------#

# 在默认情况下，参数是通过其
def f(a,b,c):
	print(a,b,c)

f(1,2,3)
# python中可以使用基于关键字的参数匹配形式
f(c=3,a=1,b=2)
# 甚至在一个调用中混合使用基于位置的参数和基于关键字的参数也可以
# 混合时只能在头部使用顺序
f(1,c=3,b=2)

# 再来说说python中的默认参数形式
def f(a,b=2,c=3):
	print(a,b,c)
f(1)
f(a=1)
f(1,4)
f(1,4,8)

# 最后一种情况，是关键字和默认参数一起使用的情况
# 只允许跳过有默认值的参数
f(1,c=6)

# 当*和**符号出现在函数定义的参数中时，表示任意数目参数收集
# 先说说*，他是用元组的形式收集不匹配的位置参数
def f2(a,*args):
	print(a,args)

f2(1,2,3,4)

# 再说说**的特性，他只对关键字参数有效，**允许将关键字参数转化为字典
def f3(**kargs):
	print(kargs)

f3(a=1,b=2)

# 在函数头部能混合一般参数、*参数以及**去实现更加灵活的调用方式。
def f4(a, *args, **kargs):
	print(a, args, kargs)

f4(1,2,3,4,5,x=6,y=7,m=8)

# 如果*和**语法出现在函数调用中，他会解包函数的集合
def func(a,b,c,d):
	print(a,b,c,d)

args = (1,2,3,4)
print(*args)
func(*args)
list = ['a','b','c','d','e','f']
print(list)
print(*list)
kargs = {'a':1, 'b':2, 'c':3, 'd':4}
# print(**kargs)
# TypeError:'a' is an invalid keyword argument for this function
func(**kargs)

# 解包混合
def func(a,b,c,d,e,f):
    print(a,b,c,d,e,f)

args = (2, 3)
kargs = {'d': 4, 'e': 5}

func(1, *args, f=6, **kargs)

# 实现对其他函数进行灵活调用
def tracer(func, *args, **kargs):
	print('calling:',func.__name__)
	return func(*args, **kargs)

def func(a,b,c,d):
	return a+b+c+d

print(tracer(func,1,2,c=3,d=4))

# print30
import sys

def print30(*args, **kargs):
	sep = kargs.pop('sep', ' ')
	end = kargs.pop('end', '\n')
	file = kargs.pop('file', sys.stdout)
	if kargs:
		raise TypeError('extra keyword:{}'.format(kargs))
	output = ''
	first = True
	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output + end)

print30('hello','world','healthy',sep='=')

#--------------------------------------------------#