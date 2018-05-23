#给妹子讲python
#S01E06

# 1.字符串的查找与替换
# 2.字符串的提取、连接与空白去除
# 3.字符串的格式化输出与类型转换
# 4.转义字符与原始字符串

#--------------------------------------------------#

# find() 找到返回偏移量，未找到返回-1
s = 'abcdef'
print(s.find('cde'))
print(s.find('fca'))

# 替换操作
s2 = 'abcdef'
print(s2.replace('bcd','xxx'))

# split()方法
s3 = 'Tom,21,USA,UCLA'
l = s3.split(',')
print(l)

s3 = 'Tom0210USA0UCLA'
l = s3.split('0')
print(l)

# join()用法
L = ['s', 'p', 'a', 'm', 'm', 'y']
sn1 = ''.join(L)
print(sn1)
sn2 = "-".join(L)
print(sn2)

# strip()

s4 = '    Tom 21 USA UCLA\n\n'
print(s4.strip())
print(s4.lstrip())
print(s4.rstrip())

# 字符串格式化输出
name = '酱油哥'
age = 28
school = ['HUST','THU']
s5 = 'name:{},age:{},and graduates from{}'.format(name,age,school)
print(s5)

s6 = '{1}, {0} and {2}'.format('spam', 'ham', 'eggs')
print(s6)

s7 = '{a}, {b} and {c}'.format(a = 'spam', b = 'ham', c = 'eggs')
print(s7)

# 格式化数字输出
s8 = 'float number = {:.2f}'.format(10.4567)
print(s8)

# 二进制输出
template = 'number = {:b}'
s9 = template.format((2 ** 16)-1)
print(s9)

# 转义符
s10 = 's\tp\nam'
print(s10)

s11 = r'c:\new\test.py'
print(s11)

# 类型转换
string = '19'
integer = 3
print(int(string) + integer)
print(bin(12))
print(int('1110',2))

#--------------------------------------------------#