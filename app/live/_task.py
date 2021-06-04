from ._live import QueryDetail, Subscribe, Report, CommentPublish, FavorRoom
import asyncio
from app import task
from ._utils import read_users


async def enter_room(user_info):
    q = QueryDetail(user_info)
    params1 = await q()
    print(params1)
    s = Subscribe(user_info, params1)
    params2 = await s()
    print(params2)

    r = Report(user_info)
    params3 = await r()
    print(f"{user_info['x-uid']}----{params3}")

    # c = CommentPublish(user_info, params1)
    # params4 = await c()
    # print(params4)

    # await asyncio.sleep(3)
    # f = FavorRoom(user_info, params1)
    # params5 = await f()
    # print(params5)


@task.add_task('live')
async def enter_live_room():
    user_info_list = read_users()

    task_list = []
    for item in user_info_list:
        task_list.append(enter_room(item))
    await asyncio.gather(*task_list)
