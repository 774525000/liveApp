from random import choices
from functools import cache


@cache
def rand_str():
    return [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)]]


@cache
def rand_global_id():
    return [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)],
            *[chr(item) for item in range(65, 91)]]


def get_rand_str(fn, k=16):
    rand_arr = fn()
    res = choices(rand_arr, k=k)
    return ''.join(res)


def get_c6():
    return get_rand_str(rand_str)


def get_utd_id():
    return get_rand_str(rand_global_id, k=24)
