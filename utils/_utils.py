from random import choices
from functools import cache


@cache
def rand_str():
    return [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)]]


@cache
def rand_global_id():
    return [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)],
            *[chr(item) for item in range(65, 91)]]


def get_rand_str(fn, k):
    rand_arr = fn()
    res = choices(rand_arr, k=k)
    return ''.join(res)


def get_lower_num(k=16):
    return get_rand_str(rand_str, k)


def get_lower_upper_num(k=24):
    return get_rand_str(rand_global_id, k)
