import asyncio
from typing import NamedTuple


async def fn(num):
    for item in range(10000):
        num.value += 1


async def run(num):
    cor_list = []
    for item in range(100000):
        cor_list.append(fn(num))
    await asyncio.gather(*cor_list)


class A:
    value: int = 0


if __name__ == '__main__':
    a = A()
    asyncio.run(run(a))
    print(a.value)
