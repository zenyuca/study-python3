# 异常处理

import logging


def foo(n):
    try:
        r = 10 / n
        print('result:', r)
    except TypeError as e:
        print('TypeError:', e)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
        # 将异常往上抛
        logging.exception(e)
        raise
    else:
        print('no error')
    finally:
        print('goon')

foo(1)
try:
    foo(0)
except BaseException as e:
    print(e)
# foo('a')
