# 给妹子讲python
# S01E17

# 1.开始编写一个简单完整的函数
# 2.函数也是对象
# 3.函数的多态内涵

#--------------------------------------------------#

# python中的函数也是对象
def func(a,b):
	return a + b

other_name = func
print(other_name(1,2))
# 函数可以被赋值给一个不同的变量名
a = print
a('cool')

# 定义(def)与调用(print(func()))
def func2(x,y):
	return x * y

print(func2(2, 4))
# 函数的运行结果取决于传递给他的值
# 这种依赖于类型的行为称为多态，操作的意义取决于被操作对象的类型
print(func2(3.14, 8))
print(func2('Ab', 8))

# 查重函数
def func3(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res

print(func3([1,2,3,4,5,6], [5,6,7,8]))
print(func3('spam', ('s', 'p', 'ac', 'e')))
print(func3([1,2,3,4], [x for x in (2,3,5)]))

# 同时我们需要注意，函数的参数是通过赋值而被传入的，
# 所以seq1和seq2是本地变量，结果列表对象是通过赋值得到的，也是本地对象，
# 所有的本地变量都在函数调用时出现，在函数退出时消失。

#--------------------------------------------------#