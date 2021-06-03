from .live import QueryDetail, Subscribe, Report
import asyncio
from app import task


async def execute_task(user_info):
    q = QueryDetail(user_info)
    res = await q()
    print(res)
    s = Subscribe(user_info, res)
    res = await s()
    print(res)

    r = Report(user_info)
    res = await r()
    print(f"{user_info['x-uid']}----{res}")


@task.add_task('live')
async def enter_live_room():
    user_info_list = [
        {
            'x-sid': '22a5639422d346970e785569e3cac400',  # c
            'x-uid': '2209572427031',
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; isg=AnR0oyDMqBGL_zxCcpAN2yJRTjDmTZg3VkBY-Q7VAP-CeRTDNl1oxyoZi4te; unb=2209572427031; sn=; uc3=nk2=F5RMGoXjyRtiUrA=&id2=UUphw2BCaFXrTatuAA==&vt3=F8dCuw75ifJ1hRePz3Y=&lg2=UtASsssmOIJ0bQ==; uc1=cookie14=Uoe2z+Ziba1G5w==&existShop=false&cookie15=U+GCWk/75gdr5Q==&cookie21=VT5L2FSpczFp; csg=3dbabf62; lgc=tb931554566; t=3ff6164b4e2f74f9a58d9dea49c60611; cookie17=UUphw2BCaFXrTatuAA==; dnk=tb931554566; skt=b6d57b2ceaf07eaf; munb=2209572427031; cookie2=22a5639422d346970e785569e3cac400; uc4=nk4=0@FY4HX7dO8Wd8xUGIADympnJwS/buEQ==&id4=0@U2grGN9Axww7kF+A9HhylLSkRntawsS4; tracknick=tb931554566; _cc_=U+GCWk/7og==; ti=; sg=61b; _l_g_=Ug==; _nk_=tb931554566; cookie1=AiAzS86U8AyQM+t18C+d5FT5KmB2ZSwxil9tZ5khPIU=; _tb_token_=e3e385504db03; sgcookie=W100/uvcZuyeVt6zmwcbrYh5ystKVGFbgyhgdDvpvwy6BHifLTKNM4PaOo0jrUsuT0sbxoXR/v4hgaJV4okTtnGbC01hrgqjMfIMRO1zwRMlybI=; imewweoriw=3HaZ7JkZkqd7bmsT0ucuZBqogJn2Qx5Qze+yt2FsgWU=; WAPFDFDTGFG=+4cMKKP+8PI+KK8XUFmnFqlIaVJQJw==; _w_tb_nick=tb931554566; ockeqeudmj=njTAsGM=; cna=FAwyGVKFSywCAXPFJohibZcS',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16226052898242238122149',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6'
        },
        {
            'x-sid': '16f3d80bc80a7170ad45ca043c6d2d02',
            'x-uid': '2100521411',
            'Cookie': 'thw=cn; unb=2100521411; sn=; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=sym3Yze86A%2FjQSg%3D&id2=UUkO1Kv%2FeCMlYQ%3D%3D&vt3=F8dCuw75ifGFagw8LxY%3D; uc1=cookie21=URm48syIYB3rzvI4Dim4&cookie14=Uoe2z%2BZl84%2B%2B2A%3D%3D&existShop=false&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; csg=f3c1eaf1; lgc=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; t=e6f2e71809317b952beedb0f0d294bc6; cookie17=UUkO1Kv%2FeCMlYQ%3D%3D; dnk=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; skt=c8ee35d043c31f49; munb=2100521411; cookie2=16f3d80bc80a7170ad45ca043c6d2d02; uc4=id4=0%40U2uCu3NZb8FJne85RaKSr2jFksZy&nk4=0%40sVYXnVU9W%2B32DLENh4iu5q6Or5eB5g%3D%3D; tracknick=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; _cc_=VT5L2FSpdA%3D%3D; ti=; sg=21d; _l_g_=Ug%3D%3D; _nk_=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; cookie1=AiBidlwPGZHvoyjWBBi2DYD0Yaidkhe6VY8HPgbAEgU%3D; _tb_token_=56e5de133b39d; sgcookie=W100HViBE8SofprkaEHpo%2FKs8kataGL2OP%2BriPVEFdZsVUYKcUPlD16c2l3XIMfwvVbI5gjRtwHbZTx%2BkUGjczbvEoXMJZaETWyXZYKE9Jbfrqo%3D; imewweoriw=366wrI2R7DzVgI7Ot%2BkbROwHPC2bKHGdnpuqZHHz2tw%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuUTJFJmnP9vVxdsYhSE6jeU%3D; _w_tb_nick=%E5%B0%8F%E7%B3%AF%E5%9B%A2%E5%AD%90712; ockeqeudmj=vp%2BZ1t4%3D; cna=fu48GefPc1ICAXrq6AxFLOBk; isg=BAUFcS-PyTNs2e1ugfaygTw_H0M_wrlUj0fpKgdqwTxLniUQzxLJJJN_rITOs9EM',
            'x-c-traceid': 'YLOUGlsA8BMDAGVXLtJVKFBF1622613916932374216628',
            'x-utdid': 'YLOUGlsA8BMDAGVXLtJVKFBF',
            'x-devid': 'AhTYPAL-iFgW659839lY5ouzoZNYld6KxhRCibjQHWel'
        }
    ]

    task_list = []
    for item in user_info_list:
        task_list.append(execute_task(item))
    await asyncio.gather(*task_list)
