#给妹子讲python
#S01E01

# 1.python中的容器数据类型概述
# 2.列表类型的异构性、有序性和本地可变性三大优势
# 2.列表的基本操作（增、删、改、分片索引）
# 3.列表的分片赋值与本地排序

#--------------------------------------------------#

#1 列表的异构性，可以装不同类型的数据
L1 = [1, 2, 3, 4, 5]
L2 = [1, 'spam', [2.3, 4]]
L3 = []

#2 有序性
L = [1,2,3,4,5,6,7,8]
print(L[1:3])

print(L[0::2])

# 对切片修改不能改变原列表的值，因为获取的L分片是一个新的独立拷贝
L = [1,2,3,4,5,6,7,8]
b = L[3:-1]
print('before change:b={}'.format(b))
b[0]=111
print('after change:b={}'.format(b))
print('after change:L={}'.format(L))

#3 本地可修改
La = [1,2,3,4]
La.append(5)
print(La)

La.insert(1,10)
print(La)

La.extend([11,22,33])
print(La)

Lb = ['aa','bb','cc','dd','ee','ff']
Lb.remove('aa')
print(Lb)

del Lb[1:3]
print(Lb)

print(Lb.pop())
print(Lb)

# 分片赋值的本质是先在原列表上删除指定分片，
# 然后在删除的位置插入新的列表，
# 因此左右两边的长度可以不等。
Lc = [4,5,6,7,8,9]
Lc[1:3] = ['aa','bb','cc','dd']
print(Lc)

# 本地排序，非作为返回值
Ld = [1,5,3,8,3,2,10]
Ld.sort()
print(Ld)
Ld.reverse()
print(Ld)

#--------------------------------------------------#