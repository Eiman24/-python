#给妹子讲python
#S01E09

# 1.文件操作模式，他的本质是字符串
# 2.文件的读方法和文件迭代器逐行扫描
# 3.文件的关闭与刷新
# 4.二进制文件的读写与对象的文件存储

#--------------------------------------------------#

# r为以只读模式打开文件，
# w为输出模式打开文件，
# a代表在文件尾部追加内容而打开文件，
# 模式字符串尾部加上b可以进行二进制数据处理，例如rb,wb,ab

# open()函数会创建一个python文件对象，作为文件操作的接口
myfile = open('myfile.txt','w')
myfile = open('myfile.txt','r')

# 写入数据
myfile = open('myfile.txt','w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

# 利用readline一次读取一行信息，
# 最后一次只返回一个空字符串说明已经到达文件底部
myfile = open('myfile.txt','r')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

# 利用read方法一次性读取全部文件内容
myfile = open('myfile.txt','r')
print(myfile.read())

# 利用for循环扫描读取每行文件
# 文件迭代器
myfile = open('myfile.txt','r')
for line in myfile:
	print(line,end='')


myfile = open('data.bin','wb')
myfile.write(b'abcdefg')
myfile.close()

data = open('data.bin','rb').read()
print(data)
print(list(data))

# pickle模块是一个通用的数据格式化和解析工具，
# 利用他可以直接在文件中储存一个字典对象和一个列表对象
import pickle
D = {'a':1,'b':2,'c':3}
L = [3,4,5]
with open('datafile.pkl', 'wb') as file:
	pickle.dump(D, file)
	pickle.dump(L, file)

# 取用这些对象，对象重建
with open('datafile.pkl', 'rb') as file:
	print(pickle.load(file))
	print(pickle.load(file))

# struct工具
import struct

F = open('data.bin','wb')
data = struct.pack('>i5sf', 8, b'abcde', 4.3)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)
# 利用unpack函数解压
values = struct.unpack('>i5sf', data)
print(values)

#--------------------------------------------------#