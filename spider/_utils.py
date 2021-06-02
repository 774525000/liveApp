from typing import NamedTuple, Union
from time import time
from urllib.parse import quote
import json


class Api(NamedTuple):
    api: str
    v: Union[int, float, str]


def dumps(obj,
          /,
          separators=(',', ':'),
          ensure_ascii=False) -> str:
    """
    序列化 json
    :param obj: 源数据
    :param separators: 分隔符
    :param ensure_ascii:  是否 ascii 编码
    :return: json 数据
    """
    return json.dumps(obj, separators=separators, ensure_ascii=ensure_ascii)


def merge_dict(obj, base_obj=None):
    """
    合并 Params
    :param obj: 要合并的 Params
    :param base_obj: 基础的 Params
    :return: 合并后的 Params
    """
    if base_obj is None:
        base_obj = {}
    return {
        **base_obj,
        **obj
    }


class Time(NamedTuple):
    millis: int
    seconds: int


def get_unix() -> Time:
    """
    获取当前毫秒级时间戳
    :return: 返回 unix 时间戳
    """
    t = time()
    t2 = t * 1000
    return Time(seconds=int(t), millis=int(t2))


def encode_headers(obj):
    cookie = obj.pop('Cookie', '')
    content_type = obj.pop('content-type', '')
    content_type_1 = obj.pop('Content_Type', '')
    obj1 = {
        key: quote(value)
        for key, value in obj.items()
    }
    return {
        **obj1,
        'Cookie': cookie,
        'content-type': content_type,
        'Content_Type': content_type_1
    }
