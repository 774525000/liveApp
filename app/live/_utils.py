import json
from random import choices
from typing import NamedTuple, Union


def read_users():
    with open('./users.json', 'r', encoding='utf-8') as f:
        res = json.load(f)
    return res


def rand_str():
    rand_arr = [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)],
                *[chr(item) for item in range(65, 91)]]
    res = choices(rand_arr, k=32)
    return ''.join(res)


class Params(NamedTuple):
    user_id: str
    user_name: str
    u_mid: str
    imei: str
    open_id: str
    live_id: str
    stay_time: Union[int, float]
