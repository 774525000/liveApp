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
            'x-sgext': 'JAGjzBEoN1F5rh3PderwD8yS/JL8ku+Q9Jf+gP2R9JTvgP2V/pb/m/6Q/pA=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAKqXuZChM/SGMFojlmvXqrzuobKJ0asP1qxXkoW4WJVUQhc0DiXDM+iUnwUXpz1DesLHu9dvhXgSuDH0VeqXqpXql6q',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1625281288093',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_fptVXtEg3e5A1haFF9qJVWP5GBoM8RN+ukFqognNbcTG+dATucM8v5yf3yIqHTmkzbXBOWMn9C3NbYukhd2NetF+O3xwfZvwwj61iPFg0tDAUCWonfnBS4q/YS7vIXDrXVu/wjKghWzvEwulqbtwbtNRP6Tk6eXhDVzMK5Pq2OI=',
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
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr1625389814949236113842',
            'x-biz-info': 'source=taobao',
            'x-location': '120.162578,30.184918',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210704000700555',
            'x-umt': 'K1gAIlBLPI+rYQJ6cMMUSyuMWEpzJdRc',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1625389814949,1625385286659,3',
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
            "liveId": user_info['live_id'],
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
            'x-sgext': 'JAFlTJHut5f5aJ0J9SxwyUxUfFR8VG9We1B5Rn9TfEZvVHpXeFd6VHtQeA==',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAI7YDy+Z+LkSEYg/gg6YDuaKK9bGdeSrqo/YKx3cFxk4dtiQUg7SZ2rwIllBSxVq9WaIH5jLytxdHH5PmY7YDtmO2A7',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1624260844726',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_kqnvEYG6PmIvaX3+GSb1DT1dxVtcI2gKtKL6QRYwq/7cpGCPGXZhUKz21HkqUt9Vakyljx+bedjmcoTjz8Rrt4kRxSWGBxVKigsHplj8uVpjVyMKKM98MfkZ3QAbLJKFzwxXXWMFOK8THkYbG0dtS3fHHWJSsw/YZau9tF9splQ=',
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
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr1624262549498104613755',
            'x-location': '120.162405,30.184992',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210621153401037',
            'x-umt': 'ygQAlxdLPF+B4AJ6KAAppsv76V5lFzWQ',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1624262549498,1624261786376,3',
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
            "liveEventsJson": "[{\"accountId\":\"790956988\",\"action\":\"enter\",\"count\":1,\"extendJson\":\"{\\\"entrySource\\\":\\\"null\\\",\\\"fansLevel\\\":\\\"0\\\",\\\"liveSource\\\":\\\"null\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"sjsdItemId\\\":\\\"null\\\",\\\"timeMovingItemId\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"0\\\"}\",\"feedId\":\"%s\",\"scene\":\"taobaolive\",\"timestamp\":\"%s\",\"type\":\"0\"}]" % (
                user_info['live_id'], ctime.millis),
            "liveId": user_info['live_id']
        }


class LeaveRoom(Spider):
    def __init__(self, user_info, params):
        ctime = get_unix()
        self.api = Api('mtop.taobao.powermsg.msg.unsubscribe', '1.0')

        topic = params['data']['topic']

        self.headers = {
            'x-sgext': 'JAH+A951+Ay289KSurc/UgPPM88zzyDPMcc3ySDNMMg03SDPNcw3zDXKNc4x',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAKkNSm9TpGeIGJ14xKpNaTPt/rETEjHMf+gNTMi7wn7tEQ33h2kHAL+X9z6ULMANIAFdeE2sH7uIe6sWwykNaSTpzWk',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1624279451748',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_uZEFuDIk92YLa8jmqDvDeOJo5EGvXV7x64Fj0p/LOvMZhRZ97e2txNcAISGQHPL9IfM0bJMjHOF8dB2yhIM7nR7nqga784Rpevx0+lba5tPg2ncCWmfpZ58typzvfKp5+o0GBgBYboe4iCOg0+Jtj6s5O0G9f/jhXW5CSSV8j0E=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16243263508827111112947',
            'x-location': '120.162575,30.184917',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210622000700971',
            'x-umt': 'ygQAlxdLPF+B4AJ6KAAppsv76V5lFzWQ',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1624326350882,1624269913650,3',
            'x-appkey': '21646297',
            'x-page-url': 'https://market.m.taobao.com/app/mtb/app-tblive-room/pages/index2',
            'x-page-name': 'https://market.m.taobao.com/app/mtb/app-tblive-room/pages/index2',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "appKey": "21646297",
            "ext": "1624326334820",
            "from": "tb931554566",
            "id": "314927152134",
            "namespace": 1,
            "role": 5,
            "sdkVersion": "0.3.0",
            "tag": "tb",
            "timestamp": ctime.millis,
            "topic": topic,
            "utdId": "YKnJdlCwF6oDACfhFIu95LNr"
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
    """
    发弹幕
    """

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


class LiveIdSpider(Spider):
    """
    通过用户名 获取 直播 id
    """

    def __init__(self):
        self.is_get = False

        ctime = get_unix()
        self.api = Api('mtop.mediaplatform.live.search.result', '1.0')

        self.headers = {
            'x-sgext': 'JAFWxhvdPaRzWxc6fx/6+sZn9mf2Z+Vl/mL0dfdv8XXlZ/Bk82X+ZPVk9Q==',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAJdFSyfE2NePvTcOdBdFV24Tc09bLHnyBFGFb1dFimiGv8XJ3NgRzjppTfjFWu++qD8VRgWSV4XAReMXhNdFV0TXRVd',
            'x-sid': '19d68831d31f0fe04e5b7f485d0df4c5',
            'A-SLIDER-Q': 'appKey=21646297&ver=1625281288093',
            'x-uid': '2209572427031',
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_tyPDwpSWXVW7+4et1J1eSvNR4WQUU2cDKlEUkUOmWPR+jX/WfCtmjdLpGL+/FmrIqISUKvj21UqLHPQhNQI7l1qvfegcfTQjkQys9XVUgPx+dBEpo4Lsp3oSOLsoWZZv4wBznDV5/vp9Re2GtjBWZ0ZJ2AjjHrTlaHSAGpa3wUY=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Length': '308',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'thw=cn; tfstk=cezcB_xiWqoYlYouAZgbiJUV01_dZ6XE3ur7zPNSRy4bAuUPi2-yXaBhIvflrh1..; l=eBOnNmL4j9ol8FX_BOfw-urza77OSCOAGuPzaNbMiOCPOQ1B5-KfW69EKLT6C3GRh62XR38XM_XWBeYBV3K-nxv99qcLxkDmn; unb=2209572427031; sn=; uc3=lg2=URm48syIIVrSKA==&vt3=F8dCuwzokVxYBahCHes=&id2=UUphw2BCaFXrTatuAA==&nk2=F5RMGoXjyRtiUrA=; uc1=existShop=false&cookie21=W5iHLLyFe3xm&cookie14=Uoe2yIF8OeAxaw==&cookie15=UIHiLt3xD8xYTw==; csg=5bfde236; lgc=tb931554566; t=cd9f2dcb95cdd61296f0ec1e7196b542; cookie17=UUphw2BCaFXrTatuAA==; dnk=tb931554566; skt=e4188644fa773e86; munb=2209572427031; cookie2=19d68831d31f0fe04e5b7f485d0df4c5; uc4=nk4=0@FY4HX7dO8Wd8xUGIADymodlCaaT9wA==&id4=0@U2grGN9Axww7kF+A9HhylLSjtiLIHW+r; tracknick=tb931554566; _cc_=U+GCWk/7og==; ti=; sg=61b; _l_g_=Ug==; _nk_=tb931554566; cookie1=AiAzS86U8AyQM+t18C+d5FT5KmB2ZSwxil9tZ5khPIU=; _tb_token_=e3e5bee08750; sgcookie=W100rr1T44ywf4AdcKSGwyMOOGEvyLbbHf6mDb9DyODH2Hh1A+bGlmnFtKOQk13/vStGjRx1LQYR2yekhjJ3nN4qVKheTLSn00/1TRQDFDUgTh0=; imewweoriw=36GQoHh1ifE7IX5a+Lyv3qdgS9EMPU4Ot8u9tGwRePk=; WAPFDFDTGFG=+4cMKKP+8PI+KK8XUFmnFqlIaVJQJw==; _w_tb_nick=tb931554566; ockeqeudmj=ttovbrU=; cna=dK9lGbWRPQACAXPDiXpb5BtQ; isg=AtfX-tcQe88o9f982dGTpgGubUkhHKt-CcFbcCkE86YNWPeaMew7zpV4yMI5',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr1625382583550048613842',
            'x-location': '120.16261,30.185052',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210704000700555',
            'x-umt': 'K1gAIlBLPI+rYQJ6cMMUSyuMWEpzJdRc',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '0,0,1625382583550,1625382321587,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/search.html',
            'x-page-name': 'com.taobao.live.TaoLiveSearchActivity',
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENtvUzl659hnIJEv_qLfu0a',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "broadCasterPageNum": "0",
            "livePageSize": "20",
            "q": "tb56371_88",
            "tabName": "live",
            "mNeedCache": "true",
            "s": "10",
            "livePageNum": "0",
            "broadCasterPageSize": "0",
            "viewversion": "3.0",
            "n": "0"
        }
