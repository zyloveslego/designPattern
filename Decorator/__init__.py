# 装饰器本质上是一个 Python 函数或类

# 插入日志、性能测试、事务处理、缓存、权限校验等场景


# 为什么有点像套娃

# 这样再套一层可以给装饰器加参数

import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="info")
def foo(name='foo'):
    print("i am %s" % name)

foo()


def decorator(func):
    def wrapper(*args, **kwargs):

        # args
        if args.User == user:

        # if level == "warn":
            logging.warn("%s is running" % func.__name__)
        # elif level == "info":
            logging.info("%s is running" % func.__name__)
        return func(*args)

    return wrapper


def decorator(func):
    print("..")
    return func


# 类修饰器调用__call__()方法
# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')
#
# @Foo
# def bar():
#     print ('bar')
#
# bar()


registry = []


def register(decorated):
    registry.append(decorated)
    return decorated


@register
def foo():
    return 3


@register
def bar():
    return 5


for i in registry:
    print(i)
    print(i())

