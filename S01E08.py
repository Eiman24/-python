#给妹子讲python
#S01E08

# 1.python中编、解码的本质是文本字符串和字节字符串的相互转换
# 2.python中编、解码方法举例及过程解析
# 3.unicode、latin-1、ASCII编码方式的兼容性问题
# 4.读取二进制文件

#--------------------------------------------------#

# 文本字符串和字节字符串
s = 'apple'
b = b'apple'
print(s)
print(type(s))
print(b)
print(type(b))

print(b[0])
print(b[1:])
print(list(b))

s1 = 'π排球の'
b1 = s1.encode('utf-8')
b2 = s1.encode()
print(b1)
print(b2)

import sys
print(sys.platform)
print(sys.getdefaultencoding())

ba = b'\xe6\x8e\x92\xe7\x90\x83'
sa = ba.decode(encoding='utf-8')
sb = ba.decode()
sc = ba.decode(encoding='latin-1')

print(sa)
print(sb)
print(sc)

ns = 'AÄBèC'

with open('utf-8data','w',encoding = 'utf-8') as f:
	f.write(ns)
with open('utf-8data','r',encoding = 'utf-8') as f:
	u_str = f.read()
print(u_str)

with open('utf-8data', 'rb') as f:
   byte_str = f.read()

print(byte_str)
print(byte_str.decode(encoding='utf-8'))

#--------------------------------------------------#