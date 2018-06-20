# 给妹子讲python
# S01E22

# 1.神奇的装饰器到底是什么
# 2.装饰器的用法和语法糖
# 3.装饰器如何添加参数

#--------------------------------------------------#

# 装饰器本质就是将原函数修饰为一个闭包(一个返回函数).

# register方法是一个简单的装饰器，
# 它把被装饰的函数添加到一个列表中，
# 然后这里是将未改变的被装饰函数返回
registry = []
def register(decorated):
	registry.append(decorated)
	return decorated

def foo():
	return 3

foo = register(foo)
print(foo)
print(registry[0])

# @register 放在定义前等价于 foo2 = register(foo2)
# 语法糖
@register
def foo2(x=3):
	return x

@register
def bar(x=5):
	return x

for func in registry:
	print(func())

# 装饰器的本质是在执行原有函数（被装饰的函数）的同时，再加上一些额外的功能。
def requires_ints(decorated):
	def inner(*args, **kwargs):
		kwarg_values = [i for i in kwargs.values()]
		for arg in list(args) + kwarg_values:
			if not isinstance(arg, int):
				raise TypeError('{} only accepts integers as arguments'.format(decorated.__name__))
		return decorated(*args, **kwargs)
	return inner


@requires_ints
def foo3(x,y):
	print(x+y)

foo3(3,5)
# TypeError
# foo3(3.4,5)

# 装饰器参数
import json

def json_output(indent=None, sort_keys=False):
    def actual_decorator(decorated):
        def inner(*args, **kwargs):
            result = decorated(*args, **kwargs)
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator

# @func()带括号的，实质上是先调用func()函数返回真正的装饰器，然后再用@进行调用。
@json_output(indent=8)
def do_nothing():
	return{'status':'done', 'func':'yes'}

print(do_nothing())

#--------------------------------------------------#