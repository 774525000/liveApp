from spider import Spider, get_unix, Api
from utils import get_lower_num


class QueryDetail(Spider):
    """
    查看直播详情
    """

    def __init__(self, user_info):
        ctime = get_unix()

        self.api = Api('mtop.tblive.live.detail.query', '4.0')

        self.headers = {
            'x-sgext': 'JAGzpns4XUETvnffH/qaH6aCloKWgoWBk4CQhYWGkYGFkJeFlIGRhJeBkIQ=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAALXU6R87IzThlikH2/VU9crHvq3KjuhQk6QU8u1nG8RzHBRrpWQ4g+piYG4JcOXOeZ2E5JQwxidR53Kw1TXU9dU11PX',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_2cIrLC+QiZg2eSP212sK61jqd3uKbkizNNpeDbxJGp+E2kKxNqx7JmENSN+LluOoKcyjGD9QX69OKdiiBwjzZCl7xr7tzqxv29ND7WJZpyOG7IhbErpdAjjSb3QlbvMk5G9u+6XVQDpAL0WK5O0iPrkdR1nPVZtJ37nDALl5d+A=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'x-biz-type': 'live',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16227726423751123125366',
            'x-biz-info': 'source=taobao',
            'x-location': '120.162505,30.184952',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210604094503394',
            'x-umt': '5xoAtRtLPIcXogJ51P45604ytlcJgDWM',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1622772642375,1622771407466,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "useLiveFandom": "true",
            "extendJson": "{\"guardAnchorSwitch\":true,\"version\":\"202003\"}",
            "ignoreH265": "false",
            "liveId": "313660834641",
            "transParams": ""
        }


class Subscribe(Spider):
    """
    进入直播间
    """

    def __init__(self, user_info, params):
        topic = params['data']['topic']
        ctime = get_unix()

        self.api = Api('mtop.taobao.powermsg.msg.subscribe', '1.0')

        self.headers = {
            'x-sgext': 'JAHsRZhnvh7w4ZSA/KV5QEXddd113WbecN9z2mbZcttmz3Tad95y23Tec9s=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAIAHfWt8r3KrqLtb1wCHQBlybRgZOzvlQBHHRz7SyHGgqcfedtHrNjnXs9vaxTZ7qihXUUeFFZKCUqEFBQAHQAUAB0A',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_l9/3TImdT3RxWfaGNtrDVSMWeonu/ScfIWQlAPvjzkruh+da4Q5b6Wa0r+Ce74e9piox160B8XSWFpX/+t1SaLJ3eQDJst9Lk4d1YEtfTJxDb4fsKIRXvbX8/MXd0EAdGLONXCUGoDnTfFDhxInSnIH79qm1n2QTgmq6NkBFO/I=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16227726519081128125366',
            'x-location': '120.162505,30.184952',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210604094503394',
            'x-umt': '5xoAtRtLPIcXogJ51P45604ytlcJgDWM',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1622772651908,1622771407466,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "appKey": "21646297",
            "ext": f"{ctime.millis}",
            "from": "小糯团子712",
            "id": user_info['x-uid'],
            "namespace": 1,
            "role": 3,
            "sdkVersion": "0.3.0",
            "tag": "tb",
            "timestamp": ctime.millis,
            "topic": topic,
            "utdId": "YKnJdlCwF6oDACfhFIu95LNr"
        }


class Report(Spider):
    def __init__(self, user_info):
        ctime = get_unix()
        self.is_get = False

        self.api = Api('mtop.taobao.iliad.event.report.batch', '2.0')

        self.headers = {
            'x-sgext': 'JAG8P+I3xE6Kse7QhvUDED+ND40PjRyOCo8JihyJB44cnw6KDY4Iiw6OCYs=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAK8tYybQ7Sx8K9MpPO+tbzNdRzczFBHKaj7taBT94l6Khu3xXP7BGRP4mfTw6hxUgAd9fm2qP72ofYsqKG8tbyhvLW8',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_WFgDhN065C0BPtUx6co81556oh+vypE712TPhvD0ql0Gcdh0BSiRd83ipOGv9f9Y2hbSSbeLGIwdI2KoRejsuaeo2IeVyt7mbEQm41/8KjtLCY8Uz/yjfCTSmWPf3UXHzKm4q87P9C63jaI2m6S5/xAdXAmP5OIJDek0rxeZ3bw=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Length': '1071',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16227726522791135125366',
            'x-location': '120.162505,30.184952',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210604094503394',
            'x-umt': '5xoAtRtLPIcXogJ51P45604ytlcJgDWM',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1622772652279,1622771407466,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "anchorId": "790956988",
            "liveEventsJson": "[{\"accountId\":\"790956988\",\"action\":\"enter\",\"count\":1,\"extendJson\":\"{\\\"entrySource\\\":\\\"null\\\",\\\"fansLevel\\\":\\\"0\\\",\\\"liveSource\\\":\\\"null\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"sjsdItemId\\\":\\\"null\\\",\\\"timeMovingItemId\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"0\\\"}\",\"feedId\":\"313660834641\",\"scene\":\"taobaolive\",\"timestamp\":\"%s\",\"type\":\"0\"}]" % ctime.millis,
            "liveId": "313660834641"
        }


class CommentPublish(Spider):
    """
    发弹幕
    """

    def __init__(self, user_info, params):
        ctime = get_unix()

        self.api = Api('mtop.taobao.iliad.comment.publish', '1.0')

        topic = params['data']['topic']

        self.headers = {
            'x-sgext': 'JAFFpNihHmYRSHUpHQyY6aR0lHSUd4d2nHWcZpN1lmaHdJJ3lnOXd5ZwlQ==',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAKl75G0obfFsZ3NNlGn76Wt8VjFlkkdMNKP72HR7tMfNIbt3CMWsFAcJc5n8eCQv1oEr+DssaTv++92pe6l76Xupe+l',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622706466102',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_OiJmKXL+9eerGplvuvmXDGWhiQRMSagOF2y5KU8q0C84ZDCnvY8U0EJoBfpwbVwuzM0rcfNfawwgteLwOWrrxVTmZNL8VF75/d7JokcTvwtVaItLdAXoLCYZukY6+phMm304FOH6nyDwNVsUy04+WcZiwC1IaUcbu+jlgy2MTOs=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YLdUQZXeZo0DAGVXLtLwfk0R1622707493411172913808',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210603160102978',
            'x-umt': 'm5oAeY5LPMwMzgJ5zF82gQPga6qexWzH',
            'x-utdid': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'c-launch-info': '3,0,1622707493411,1622632241270,2',
            'x-appkey': '21646297',
            'x-page-url': 'https://market.m.taobao.com/app/mtb/live-commodity/pages/index',
            'x-page-name': 'https://market.m.taobao.com/app/mtb/live-commodity/pages/index',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "renders": "{\"fanLevel\":\"2\"}", "topic": topic,
            "content": "你好呀"}


class FavorRoom(Spider):
    """
    直播间点赞
    """

    def __init__(self, user_info, params):
        ctime = get_unix()

        self.api = Api('mtop.taobao.iliad.recommend.publish', '1.0')

        self.headers = {
            'x-sgext': 'JAHM3qIoZO9rwQ+gZ4XiYN797v3u/v3/5vzm7+/67Pn97+/67P7o/+z+6/0=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAJbJoS9jdI5TAmGMH9dJltkD5E7X7fUzhtxJp8YEBrh/XgkIuroea7V2weZOB5ZQZP6Zh4lT20RMhG/SyJbJlsiWyZb',
            'x-sid': user_info['x-sid'],
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_jd3d8BpiygBrP+HqMhEz5x8iLheF1chwKYKx77TnZp6SsiyOqsQ1oCK2fR/+E6fxD3ONQcPyP6j3OWLus8kotHlIa63xbgjzTBrCkwpgRBXQpXiBpv2D0agrucHjWzfTpJNjizPsLfdTjm2aOWOFR+Mjp2e58c+xmZ5wOutp31A=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YLdUQZXeZo0DAGVXLtLwfk0R1622709859118356713808',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210603163603566',
            'x-umt': 'm5oAeY5LPMwMzgJ5zF82gQPga6qexWzH',
            'x-utdid': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'c-launch-info': '3,0,1622709859118,1622632241270,2',
            'x-appkey': '21646297',
            'x-page-url': 'https://market.m.taobao.com/app/mtb/app-tblive-room/pages/index2',
            'x-page-name': 'https://market.m.taobao.com/app/mtb/app-tblive-room/pages/index2',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        topic = params['data']['topic']

        self.data = {"count": "10", "topic": topic}


class SendMsg(Spider):
    def __init__(self):
        ctime = get_unix()

        self.api = Api('mtop.taobao.powermsg.msg.sendmsg', '1.0')

        self.headers = {
            'x-sgext': 'JAEiBdip/tCwL9ROvGs5jgUTNRM1EyYaNxE9AT0SPAEmEzMQNhI2ETwbMQ==',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAALgfWsIXr2v2i8+LlTjfeAFKdSABAyPdea8feAkq0HAKU9/mZ17N9zBisRBQZTz3MhBPaV+9Daqaark8XbgfeB24H3g',
            'x-sid': '2775809838c2887a187b91f506e8c92d',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622981502612',
            'x-uid': '2209572427031',
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_1fuvjVTTrCjF20qT/cIoSsnsIb4aDZJougS+CjimxfOZek9yvIwhmHWTyDVwO9i+cRW7hA4R0OrPsJ9Q5Zmlc3QA1GZQAzwFHtAm5/ROXx4BawWaD5ePKNUPHf84m90zAgTdYH5E8hnAuAN1nbeu2XOGdcKcoT+f/G7uu5oW7Dc=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; _m_h5_tk=99e0959ecd066654051d0c1a4c054abd_1622800022257; _m_h5_tk_enc=8dfa8559ab5b9406b94066194c9af68b; xlly=1; unb=2209572427031; sn=; uc3=vt3=F8dCuw7+gb+rbuIvHeY=&id2=UUphw2BCaFXrTatuAA==&nk2=F5RMGoXjyRtiUrA=&lg2=VT5L2FSpMGV7TQ==; uc1=cookie14=Uoe2zsmzzvtzyg==&cookie15=WqG3DMC9VAQiUQ==&cookie21=VFC/uZ9ainBZ&existShop=false; csg=7ac735ed; lgc=tb931554566; t=46a9cbd2288b23388130ed713a76b739; cookie17=UUphw2BCaFXrTatuAA==; dnk=tb931554566; skt=1a5c938a899c6db5; munb=2209572427031; cookie2=2775809838c2887a187b91f506e8c92d; uc4=id4=0@U2grGN9Axww7kF+A9HhylLSlKE12GYeX&nk4=0@FY4HX7dO8Wd8xUGIADymp6EtntfFow==; tracknick=tb931554566; _cc_=Vq8l+KCLiw==; ti=; sg=61b; _l_g_=Ug==; _nk_=tb931554566; cookie1=AiAzS86U8AyQM+t18C+d5FT5KmB2ZSwxil9tZ5khPIU=; _tb_token_=ee561655b6eef; sgcookie=W100ZXpWS19OYAioKT9B3UxWHPQamMvlReMQ66KcKam955HUrL5TuvOfJtCEyjiVMJNf5BOJf76HGSipSBIy4FPVLg93mJCgs/mvj6bfJuu0NL8=; imewweoriw=3HOahQlaA1sKWUlyf+smbmou09pzC0swSeFP1vhdIEg=; WAPFDFDTGFG=+4cMKKP+8PI+KK8XUFmnFqlIaVJQJw==; _w_tb_nick=tb931554566; ockeqeudmj=j+0GVTk=; cna=FAwyGVKFSywCAXPFJohibZcS; isg=BJ6eJFyNcnSpnaYEtMKHZRzj5DbgX2LZeBJiP0gnCuHcaz5FsO-y6cQKZzFFolrx',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr1623035329842178218238',
            'x-location': '120.162393,30.184997',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210607103201067',
            'x-umt': 'm1wAAFlLPCBUrwJ54JtKPLxquaE8dI48',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1623035329842,1623033985470,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "msgId": get_lower_num(32),  # 这个要随机生成
            "namespace": 1,
            "qos": 0,
            "sdkVersion": "0.3.0",
            "sendAll": False,
            "subType": 10010,
            "tagList": "[]",
            "topic": "bc2dfd00-fe1e-47b7-a5d6-3f09276c732d"
        }
