#给妹子讲python
#S01E15

# 1.使用迭代协议的逐项扫描工具可以称之为迭代环境
# 2.迭代环境还包含很多可以传入可迭代对象的内置方法
# 3.常用迭代环境：列表解析式
# 4.可迭代对象优势总结

#--------------------------------------------------#

# 迭代对象中只有sorted函数的结果是返回一个真正的列表
print(sorted(open('myfile.txt')))

# 一般意义上，能从左到右的扫描一个对象的各种工具，实质上都在主体对象上使用了迭代协议
# 包括了list和tuple、set内置函数，还有字符串的join方法甚至赋值
print(list(open('myfile.txt')))
print(tuple(open('myfile.txt')))
print('$$'.join(open('myfile.txt')))
a,b,c = open('myfile.txt')
print(a,b,c)

# 列表解析式也是最常应用迭代协议的环境之一
L = [1,2,3]
L1 = [x+3 for x in L]
print(L1)

# 这种列表解析的方式比手动的for循环更快，
# 因为他们的迭代在解释器内部是以C语言的速度执行的。
lines = [line.rstrip() for line in open('myfile.txt')]
print(lines)


# 根据需要产生数据，而不是在内存中构建一个结果列表，
# 从而达到节约内存空间的目的，这是可迭代对象最重要的好处。

#--------------------------------------------------#