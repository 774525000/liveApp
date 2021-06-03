
from pathlib import Path
import json


def dumps_cookies(cookie_list: list[str]) -> str:
    cookie_str = 'thw=cn'
    for item in cookie_list:
        cookie_item = item.split(';', 1)
        cookie_str += f'; {cookie_item[0]}'
    return cookie_str


def save_user_info(params1, params3):
    data = params3['data']['returnValue']['data']
    res = json.loads(data)

    cookie_list = res['cookies']
    cookies = dumps_cookies(cookie_list)
    path = Path('./users.json')
    if path.exists():
        with open('./users.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    else:
        data_list = []

    data_list.append({
        'x-sid': res['sid'],
        'x-uid': str(res['userId']),
        'Cookie': cookies,
        'x-devid': params1['data']['device_id'],
        'mobile': res['phone'],
        'nick': res['nick']
    })

    with open('./users.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)
