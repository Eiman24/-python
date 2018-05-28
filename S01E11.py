#给妹子讲python
#S01E11

# 1.可变对象的原处修改
# 2.如何获取对象的独立复制
# 3.比较、相等性和真值问题

#--------------------------------------------------#

# 原处修改会影响引用这个对象的其他变量
X = [1,2,3,4,5]
L = ['a', X, 'b']
D = {'x':X, 'y':2}

L[1][2] = 'changed'
print(X)
print(L)
print(D)

# 分片操作可以复制列表
L = [1,2,3,4,5]
C = L[:]
C[0] = 8
print(L)
print(C)

# 字典的copy方法实现完全复制
D = {'a':1, 'b':2}
B = D.copy()
B['a'] = 888
print(D)
print(B)

# 内置函数list可以生成拷贝
L = [1,2,3,4]
C = list(L)
C[0] = 888
print(L)
print(C)

# 浅拷贝只拷贝顶层的对象
L = [1,2,3,4]
A = [1,2,3,L]
B = A[:]
B[1] = 333
B[3][1] = ['changed']
print(A)
print(B)
print(L)

# 通过深拷贝完成整体拷贝
import copy

L = [1,2,3,4]
A = [1,2,3,L]
B = copy.deepcopy(A)
B[1] = 333
B[3][1] = ['changed']
print(A)
print(B)
print(L)

# 测试是否对象一致性，需要确定是否在一个内存空间
L1 = [1,2,['A','B']]
L2 = [1,2,['A','B']]
L3 = L1
print(L1 == L2, L1 is L2)
print(L1 == L3, L1 is L3)

# Python把任意的空数据结构视为假，把任何非空数据结构视为真

L = [None] * 10
print(L)
for i in range(len(L)):
	print(bool(L[i]))

print(bool([1,2]))
print(bool(True))
print(bool(None))
print(bool('abcde'))

#--------------------------------------------------#