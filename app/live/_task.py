from ._live import QueryDetail, Subscribe, Report, CommentPublish, FavorRoom, SendMsg, LeaveRoom, LiveIdSpider
import asyncio
from app import task
from ._utils import read_users, rand_str, Params
from ._upload import live_upload, keep_live_upload
from random import randint


async def enter_room(user_info):
    q = QueryDetail(user_info)
    res1 = await q()
    print(res1)
    s = Subscribe(user_info, res1)
    res2 = await s()
    print(res2)

    r = Report(user_info)
    res3 = await r()
    print(f"{user_info['x-uid']}----{res3}")
    #
    # await asyncio.sleep(10)
    #
    # leave_room = LeaveRoom(user_info, params1)
    # params4 = await leave_room()
    # print(params4)
    #
    # c = CommentPublish(user_info, params1)
    # params4 = await c()
    # print(params4)
    #
    # await asyncio.sleep(3)
    # f = FavorRoom(user_info, params1)
    # params5 = await f()
    # print(params5)
    # send_msg = SendMsg()
    # res = await send_msg()
    # print(res)

    # 日志包 观看人数，以及停留时间都在 日志包中 体现
    params = Params(
        user_info['x-uid'],
        user_name=user_info['nick'],
        u_mid=rand_str(),
        imei=f'3536270780{randint(10000, 100000)}',
        open_id=user_info['open_id'],
        live_id=user_info['live_id'],
        stay_time=500000
    )

    res = await live_upload(params)
    print(f"{user_info['nick']}----{res}")

    # while True:
    #     res = await keep_live_upload(params)
    #     print(f"{user_info['nick']}----{res}")
    #     await asyncio.sleep(10)


@task.add_task('live')
async def enter_live_room():
    live_id_spider = LiveIdSpider()
    res = await live_id_spider()
    live_id = res['data']['cardList'][0]['cardData'][0]['liveInfo']['liveId']
    print(f'直播id：{live_id}')

    task_list = []
    user_info_list = read_users()
    for item in user_info_list:
        item['live_id'] = live_id
        task_list.append(enter_room(item))
    await asyncio.gather(*task_list)
