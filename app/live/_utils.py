import json


def read_users():
    with open('./users.json', 'r', encoding='utf-8') as f:
        res = json.load(f)
    return res
