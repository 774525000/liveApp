from pathlib import Path
import aiofiles
from functools import wraps
import gzip
from hashlib import md5
from ._spider import Spider


async def read_log(filename: str):
    path = Path('./assets') / filename
    if not path.exists():
        raise FileExistsError(f'{filename} is not exists')
    async with aiofiles.open(path, 'r', encoding='utf-8') as f:
        return await f.read()


def encode(str_: str) -> bytearray:
    str_ = str_.strip()
    str_list = str_.split("\n\n")
    if len(str_list) <= 1:
        raise ValueError("值错误")

    total_byte_list = bytearray()
    common_str = str_list[0]
    content_list = str_list[1:]

    content = bytearray(common_str.encode("utf-8"))
    content_len = len(content).to_bytes(2, 'big')

    total_byte_list.append(content_len[0])
    total_byte_list.append(content_len[1])

    for item in content:
        total_byte_list.append(item)

    for item in content_list:
        key_value_list = item.split(":-----\n")
        key_ = int(key_value_list[0])
        value = key_value_list[1]

        key_byte_list = key_.to_bytes(4, 'big')

        value_string_list = value.strip().split("\n")

        byte_list_item = bytearray()
        for value_item in value_string_list:
            for value_item_byte in bytearray(value_item.encode("utf-8")):
                byte_list_item.append(value_item_byte)
            byte_list_item.append(1)
        byte_list_item.pop()

        for item1 in key_byte_list:
            total_byte_list.append(item1)

        content_len_byte_list = len(byte_list_item).to_bytes(4, 'big')
        for item2 in content_len_byte_list:
            total_byte_list.append(item2)

        for item3 in byte_list_item:
            total_byte_list.append(item3)

    zip_list = gzip.compress(total_byte_list, 6)
    zip_len_byte_list = len(zip_list).to_bytes(4, 'big')

    all_data_list = bytearray(
        [0x01, *zip_len_byte_list[1:], 0x01, 0x29, 0x00, 0x00, *zip_list])

    for item in range(12, 18):
        all_data_list[item] = 0x00

    return all_data_list


async def encode_x_s(data: bytearray) -> str:
    x_s_params = md5(data).hexdigest().lower()
    res = await Spider.get_client().get('http://192.168.0.140:10086/getSign', params={
        'p1': x_s_params
    })
    return res.text


def upload(file_name, url='https://h-adashx.ut.taobao.com/upload'):
    def f1(fn):
        @wraps(fn)
        async def f2(params, *args, **kwargs):
            data_str = await read_log(file_name)
            has_format = fn(data_str, params, *args, **kwargs)
            if has_format:
                data_str = has_format

            encoded_data = encode(data_str)

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Charset': 'UTF-8',
                'x-k': '21646297',
                'x-s': await encode_x_s(encoded_data),
                'x-t': '1',
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)',
                'Host': 'h-adashx.ut.taobao.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
            }

            res = await Spider.get_client().post(url, content=bytes(encoded_data), headers=headers)
            return res.text

        return f2

    return f1
