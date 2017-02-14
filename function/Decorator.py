# 装饰器

import time
import functools


def now():
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return str(time.time())


def log(func):
    def wrapper(*args, **kw):
        print('Call: ' + func.__name__ + '()')
        a = now()
        print('Begin: ' + a)
        func(*args, **kw)
        b = now()
        print('End: ' + b)
        print('Execute time: %fs' % (float(b) - float(a)))
    return wrapper


@log
def func():
    for i in range(100000):
        # print(i)
        pass

func()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def func():
    for i in range(10000):
        # print(i)
        pass

func()
print(func.__name__)      # => wrapper 并不是 func


def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('Call %s()' % func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('Call %s()' % text.__name__)
            return text(*args, **kw)
        return wrapper


@log('abc')
def func():
    pass

func()
print(func.__name__)      # => func
