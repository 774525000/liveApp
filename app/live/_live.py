from spider import Spider, get_unix, Api


class QueryDetail(Spider):
    """
    查看直播详情
    """

    def __init__(self, user_info):
        ctime = get_unix()

        self.api = Api('mtop.tblive.live.detail.query', '4.0')

        self.headers = {
            'x-sgext': 'JAG5D9Iy9Eu6tN7VtvAzFQ+IP4g/iCyLPYg7gCyBO40smj6PPYs6ijeKP44=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAKxTRw5+oF3ZG2OmwGyTbE1eOTRNF2/JFD2Ta2r+nF30hZPyIv2/Gm375/eO6WJX/gQDfROpQb7WfvUTkSxTbEWtU2x',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622605294045',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-m-biz-live-bizcode': 'TAOBAO',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_QuC9OyP7B5NWDYx/yxa5iDCc9Kka/EO8Ja+wtaLFkZiHkza6wtqySnZOx+xjCd1vYdSpUZXLNlMll2tYaY7AYadzHzJ7PyHPEpbrFmRDXPpTbeAivUoxgsQLJj9vWBVPTtHwAyXFeX8KeghAk8/jG54OnTBQNMixfs10vRUsXyU=',
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
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16226052898242238122149',
            'x-biz-info': 'source=taobao',
            'x-location': '120.162405,30.184988',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210602113200236',
            'x-umt': 'HUcAHOZLPMafpwJ5xkex2Ppe0m92FMTu',
            'x-utdid': 'YLOUGlsA8BMDAGVXLtJVKFBF',
            'c-launch-info': '3,0,1622605289824,1622538313482,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {"useLiveFandom": "true", "extendJson": "{\"guardAnchorSwitch\":true,\"version\":\"202003\"}",
                     "ignoreH265": "false", "liveId": "311734092779", "transParams": ""}


class Subscribe(Spider):
    """
    进入直播间
    """

    def __init__(self, user_info, params):
        topic = params['data']['topic']
        ctime = get_unix()

        self.api = Api('mtop.taobao.powermsg.msg.subscribe', '1.0')

        self.headers = {
            'x-sgext': 'JAHwA957+AK2/dKcurk/XAPBM8EzwSDCMcE3ySDIN8kg0zLGMcI2wzvDM8c=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAALAJUssr5ODrtDQOHTDJcBdCYygXCzXVTiHJdzDixkGumcnueOHlBjfnvevU9ThLpBhZYUm1G6KMYq8PzXAJcB+xCXA',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622605294045',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_VKynnXmeuNCx3KGhb42AB8xvzX+j1gSbxi6KS4pB403WHKcClBGfiyvCVus+arS5ErkiRNzcrmZYXbQF2vPbI97N9ATQX6kSNJqEKo33qyGHVhzvGV2oQIDbFBe/iHYDsONsp5NKgd4cZ/31IzGAOrpredABWzc98jo1kL4UDFg=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16226052898242238122149',
            'x-location': '120.162405,30.184988',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210602113200236',
            'x-umt': 'HUcAHOZLPMafpwJ5xkex2Ppe0m92FMTu',
            'x-utdid': 'YLOUGlsA8BMDAGVXLtJVKFBF',
            'c-launch-info': '3,0,1622605290531,1622538313482,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {"appKey": "21646297", "ext": f"{ctime.millis}", "from": "tb931554566", "id": user_info['x-uid'],
                     "namespace": 1, "role": 3, "sdkVersion": "0.3.0", "tag": "tb", "timestamp": ctime.millis,
                     "topic": topic, "utdId": 'YLOUGlsA8BMDAGVXLtJVKFBF'}


class Report(Spider):
    def __init__(self, user_info):
        ctime = get_unix()
        self.is_get = False

        self.api = Api('mtop.taobao.iliad.event.report.batch', '2.0')

        self.headers = {
            'x-sgext': 'JAEyzBG5N8B5Px1edXvwnswD/AP8A+8A/gP4C+8K+QHvEf0E/gD5AfQB/AU=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAKOZ5bMHFzJEBP9vjKNZ44fR87uHmKVG3rJZ5KBxVtI+Cll96HJ1lad0LXhEZqjYNIvJ8tkmizEc8T+cWiOZ448imeO',
            'x-sid': user_info['x-sid'],
            'A-SLIDER-Q': 'appKey=21646297&ver=1622605356557',
            'x-uid': user_info['x-uid'],
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_Pdhduw5w95OV7zJliq0BQA5vY5tg7aHBc7Tw7tbaYnmgHG8GiCcpOZffS0R8ldV5k4FZqktlXt2j5jsjC69NsL6oqJ1YPJUzvoJBdWy8wG73yndenfD5DlugqmkE+z7bKeUlWZe3IRHMbUaf4X9ac3csHfmVYY0WMG6G0geZ9MY=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': user_info['Cookie'],
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16226052898242238122149',
            'x-location': '120.162405,30.184988',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210602113200236',
            'x-umt': 'HUcAHOZLPMafpwJ5xkex2Ppe0m92FMTu',
            'x-utdid': 'YLOUGlsA8BMDAGVXLtJVKFBF',
            'c-launch-info': '3,0,1622605291026,1622538313482,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://h5.m.taobao.com/taolive/video.html',
            'x-page-name': 'com.taobao.taolive.room.TaoLiveVideoActivity',
            'x-devid': user_info['x-devid'],
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {"anchorId": "790956988",
                     "liveEventsJson": "[{\"accountId\":\"790956988\",\"action\":\"enter\",\"count\":1,\"extendJson\":\"{\\\"entrySource\\\":\\\"null\\\",\\\"fansLevel\\\":\\\"0\\\",\\\"liveSource\\\":\\\"null\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"sjsdItemId\\\":\\\"null\\\",\\\"timeMovingItemId\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"0\\\"}\",\"feedId\":\"311734092779\",\"scene\":\"taobaolive\",\"timestamp\":\"%s\",\"type\":\"0\"}]" % ctime.millis,
                     "liveId": "311734092779"}


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
