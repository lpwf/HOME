from functools import lru_cache
from collections.abc import Callable


def cache(times):
    cache = {}
    def x(func: Callable):
        def wrapper(*args, **kwargs):
            wrapper.times=times
            if not cache.get(args) and wrapper.times==0:
                func_result = func(*args, **kwargs)
                cache[args] = func_result
                return func_result
            else:
                wrapper.times -= 1
                return cache[args]

        return wrapper
    return x


def cache_lru(func: Callable) -> Callable:
    return lru_cache(func)




@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead
print(f())
print(f())
print(f())
print(f())
print(f())