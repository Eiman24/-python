#给妹子讲python
#S01E14

# 1.可迭代对象、迭代器、迭代协议是什么
# 2.实际序列和循环中按需逐次产生结果的对象都是可迭代对象
# 3.手动模拟迭代过程
# 4.可迭代对象举例：文件、字典、range及enumerate返回值

#--------------------------------------------------#

# 可迭代对象分为两大类
# 1.实际保存序列的对象，如列表元组
# 2.按需产生虚拟序列的对象，如range，zip 

# 利用iter函数对可迭代对象调用iter函数会返回一个迭代器
L = [2, 3, 4]
I = iter(L)
print(iter(L))
print(I)
print(I is L)
# 对迭代器进行iter调用会返回其自身,
# 可以通过这个方法检验是否为可迭代对象
print(I is iter(I))
print(iter(I))

# 迭代协议
L = [2, 3, 4]
I = iter(L)
print(next(I))
print(next(I))
print(next(I))
# StopIteration
#print(next(I))

# 文件也是可迭代对象
f = open('myfile.txt')
print(f is iter(f))

f = open('myfile.txt')
print(next(f))
print(next(f))
print(next(f))
# StopIteration
#print(next(f))
 
f = open('myfile.txt')
for line in f:
	print(line, end='')

f = open('myfile.txt')
for line in f.readlines():
	print(line, end='')

# 字典也是可迭代对象
D = {'a':1, 'b':2, 'c':3}
I = iter(D)
print(next(I))
print(next(I))
print(next(I))
# StopIteration
#print(next(I))

D = {'a':1,'b':2,'c':3}
print(D.keys())
print(iter(D.keys()))
print(D.values())
print(iter(D.values()))
print(D.items())
print(iter(D.items()))

# range迭代对象
R = range(5)
I = iter(R)
print(R)
print(I)

# enumerate迭代对象
E = enumerate('spam')
print(E)
print(iter(E))

print(list(enumerate('spam')))

#--------------------------------------------------#