#给妹子讲python
#S01E02

# 1.字典的动态生成方法及字典的合并
# 2.字典键不存在时的处理技巧
# 3.一次性高效获取键、值列表方法举例
# 4.字典的删除与排序

#--------------------------------------------------#

# 异构型，无序性
DBM = {
	'name' : {'first':'Bob', 'last':'marley'},
	'job' : ['musician','reggae'],
	'age' : 46.5,
	'addr' : 'Jamaica'
}
print(DBM)

# 字典读取与修改
D1 = {'food':'spam', 'quality':4, 'color': 'pink'}
print(D1['food'])
D1['sex'] = 'gender'
print(D1)
D1['food'] = 'pizza'
print(D1)

# 初始化字典

# 第一种：空字典填充键值
D2 = {}
D2['name'] = 'Bob'
D2['job'] = 'singer'
print(D2)

# 第二种：zip列表方法
key_list = ['a','b','c']
value_list = [11,22,33]
D3 = dict(zip(key_list, value_list))
print(D3)

# 第三种：键值对元组构造
D4 = dict([('aa', 11),('bb',22),('cc',33)])
print(D4)

# 字典的合并
# 两个字典中有冲突的键，那么会无规律的进行覆盖
Dl = {'a':1,'b':2, 'c':3}
Dr = {'c':8, 'd':9}
Dl.update(Dr)
print(Dl)

# 字典的in用法
D5 = {'a':1, 'b':2}
print('c' in D5)
if not 'c' in D5:
	print('Missing')

# get用法 第二个参数为键不存在返回的默认值，如果不设置返回None
D6 = {'a':11,'b':22, 'c':33}
print(D6.get('a',0))
print(D6.get('d',0))

# 一次性获取所有的键,值，键值对； keys(),values(),items()返回的是迭代器
D7 = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
print(D7.keys())
print(list(D7.keys()))

print(D7.values())
print(list(D7.values())) 

print(D7.items())
print(list(D7.items()))

# 字典删除
D8 = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
del D8['a']
print(D8)
print(D8.pop('b'))
print(D8)

# 字典的排序,实际上是为键进行排序,想具体排序利用keys()和values()
# sorted()其实接受的都是可迭代对象
D9 = {'b': 22, 'a': 11, 'c': 33, 'e': 55, 'd': 44}
print(sorted(D9))
print(sorted(D9.keys()))
print(sorted(D9.values()))

#--------------------------------------------------#