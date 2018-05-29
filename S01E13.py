#给妹子讲python
#S01E13

# 1.range函数：返回一系列连续增加的整数
# 2.zip函数：并行迭代多个序列
# 3.enumerate函数：同时产生偏移和元素

#--------------------------------------------------#

for i in range(5):
	print(i, end=',')

print(range(5))
print(list(range(-5,5)))


S = 'abcdefghijklmn'
for i in range(0, len(S),2):
	print(S[i], end=',')

S = 'abcdefghijklmn'
for c in S[::2]:
	print(c, end=',')

# 需要在遍历中得到结果，也可以利用list()
L1 = [1,2,3,4,5]
L2 = ['A','B','C','D','E']
for t in zip(L1, L2):
	print(t, end=',')

print(zip(L1, L2))

print(list(zip(L1, L2)))

# zip只选择最短的序列长度
L1 = [1,2,3,4,5]
L2 = ['A','B','C']
print(list(zip(L1,L2)))

# 生成字典
keys = ['A', 'B', 'C']
vals = [1, 2, 3]
D = dict(zip(keys, vals))
print(D)

# 显示对应元素以及其偏移量
S = 'spam'
for t in enumerate(S):
	print(t, end='')
# 迭代器
print(enumerate(S))

L = ['a', 'b', 'c', 'd', 'e']
for t in enumerate(L):
	print(t, end='')

#--------------------------------------------------#