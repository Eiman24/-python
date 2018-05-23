#给妹子讲python
#S01E05

# 1.字符串支持一些容器的基本操作，如分片索引
# 2.字符串的不可修改特性
# 3.字符串的连接、遍历和成员测试
# 4.字符串赋值操作中的深拷贝与浅拷贝

#--------------------------------------------------#

# 字符串的切片操作
s = 'abcdefg'
print(s[0])
print(s[-2])
print(s[1:4])
print(s[1:4:2])
print(s[-1:1:-1])
print(len(s))

# 两个字符连接
s1 = 'abcd'
s2 = '1234'
s = s1 + s2
print(s)

# 深拷贝，储存的值相同但存储在不同的内存区域
s3 = ['abcdefg']
a = s3[:]
print(a)
print(s is a)

# 浅拷贝 sl与sr两个对象实际被分排在同一个内存区域内
sl = 'abcdefg'
sr = sl
print(sl is sr)

# 循环迭代
s = 'hacker'
for c in s:
	print(c, end='')

print('k' in 'school')

#--------------------------------------------------#