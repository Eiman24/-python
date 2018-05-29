#给妹子讲python
#S01E12

# 1.for循环的用法范例
# 2.while循环的用法范例
# 3.字典和文件的迭代用法举例

#--------------------------------------------------#

# while循环
a = 0
b = 10
while a < b:
	print(a, end=',')
	a = a + 1
print('\n')

# continue跳出本轮循环，从循环主体顶部再次开始
a = 0
b = 10
while a < b:
	a = a + 1
	if a % 2 != 0:
		continue
	print(a, end=',')
print('\n')

# break直接跳出循环
a = 0
b = 10
while a < b:
	a = a + 1
	if a == 5:
		break
	print(a, end=',')
print('\n')

# else:当循环体没有break时执行else语句
for y in [33, 29]:
	x = y // 2
	while x > 1:
		if y % x == 0:
			print('{} has a factor {}'.format(y, x))
			break
		x = x - 1
	else:
		print('{} is prime'.format(y))

# 字典对象不是有序的但可以通过for来遍历
D = {'a':1, 'b':2, 'c':3}
for key in D:
	print(key,'--->',D[key])
# items()方法
for (key, value) in D.items():
	print(key,'--->',value)

# 调用文件对象的read方法
file = open('myfile.txt', 'r')
print(file.read())

# 逐行遍历
# 1.一次性将文件全部载入字符串列表中
for lines in open('myfile.txt', 'r').readlines():
	print(lines,end='')
print(open('myfile.txt', 'r').readlines())

# 2.利用迭代器循环到哪一行就读取哪一行，节省内存
for lines in open('myfile.txt', 'r'):
	print(lines,end='')
print(open('myfile.txt', 'r'))

#--------------------------------------------------#