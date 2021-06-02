from app import enter_live_room, auto_login
from spider import Spider
import asyncio


async def run():
    async with Spider() as _:
        await auto_login()


if __name__ == '__main__':
    asyncio.run(run())
