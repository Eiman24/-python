#给妹子讲python
#S01E16

# 1.生成器函数的使用
# 2.生成器表达式的使用
# 3.与列表解析式的对比及对内存的优化

#--------------------------------------------------#

# 生成器函数返回了一个迭代器，
# yield语句一次返回一个结果
def gen_squares(num):
	for x in range(num):
		yield x ** 2

G = gen_squares(5)
print(G)
print(iter(G))

# 手动模拟
G = gen_squares(3)
print(G)
print(iter(G))
print(next(G))
print(next(G))
print(next(G))
# StopIteration
# print(next(G))

for i in gen_squares(5):
	print(i, end=' ')
	print()

for i in gen_squares(4):
	print('x ** 2 = {}'.format(i))
	print('--------------------')

# 生成器表达式为圆括号，列表的解析式方括号
print([x ** 2 for x in range(5)])
print((x ** 2 for x in range(5)))
# 生成器表达式支持迭代协议，适用于所有迭代环境
for x in (x ** 2 for x in range(5)):
	print(x, end=',')
print(sum(x ** 2 for x in range(5)))
print(sorted((x ** 2 for x in range(5)), reverse = True))
print(list(x ** 2 for x in range(5)))

# 生成器与解析式: 列表解析式最快，生成器表达式最省空间，速度也还可以。

#--------------------------------------------------#