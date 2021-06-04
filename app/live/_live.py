from spider import Spider, get_unix, Api


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
            'x-sid': '1b5bc95e650d265b1d8159b38b544c77',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': '2100521411',
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
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; unb=2100521411; sn=; uc3=vt3=F8dCuw76qoBME0VRJPk%3D&id2=UUkO1Kv%2FeCMlYQ%3D%3D&nk2=sym3Yze86A%2FjQSg%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; uc1=cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie14=Uoe2z%2BTLhW13lw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false; csg=bae1b678; lgc=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; t=a2b917c50bd04e33a3a3f98c9b4961df; cookie17=UUkO1Kv%2FeCMlYQ%3D%3D; dnk=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; skt=2f3d81f56f5c16b0; munb=2100521411; cookie2=1b5bc95e650d265b1d8159b38b544c77; uc4=id4=0%40U2uCu3NZb8FJne85RaKSrX7%2FPDS8&nk4=0%40sVYXnVU9W%2B32DLENh4iu5qxpUlckKQ%3D%3D; tracknick=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; _cc_=VFC%2FuZ9ajQ%3D%3D; ti=1568860058617%40taobao_android_9.25.0; sg=21d; _l_g_=Ug%3D%3D; _nk_=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; cookie1=AiBidlwPGZHvoyjWBBi2DYD0Yaidkhe6VY8HPgbAEgU%3D; _tb_token_=ee4b8b383bde; sgcookie=W100z3Cb7qXZSW%2FJp98oc1goxkI6uHOzvW7PndgX0mkI8t%2FOiKraPhPFdoK6pfwGOCy0yTfOMbZakUDhOfEWNXN2rMOuvQxkiyjK2%2F3MzNg7ZOU%3D; imewweoriw=3%2FqcKUC8ML9xucTzN5%2B2W6LA9%2BxNQdXdHyjfcgTjBFU%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuUTJFJmnP9vVxdsYhSE6jeU%3D; _w_tb_nick=%E5%B0%8F%E7%B3%AF%E5%9B%A2%E5%AD%90712; ockeqeudmj=r4pchfM%3D; cna=FAwyGVKFSywCAXPFJohibZcS; isg=AhUVQH1-2e2Nnv0Byz_8iFumLxPPEskkH_fZ-pe60Qzb7jXgX2LZ9COuysgn',
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
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "useLiveFandom": "true",
            "extendJson": "{\"guardAnchorSwitch\":true,\"version\":\"202003\"}",
            "ignoreH265": "false",
            "liveId": "311734092779",
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
            'x-sid': '1b5bc95e650d265b1d8159b38b544c77',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': '2100521411',
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
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; unb=2100521411; sn=; uc3=vt3=F8dCuw76qoBME0VRJPk%3D&id2=UUkO1Kv%2FeCMlYQ%3D%3D&nk2=sym3Yze86A%2FjQSg%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; uc1=cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie14=Uoe2z%2BTLhW13lw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false; csg=bae1b678; lgc=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; t=a2b917c50bd04e33a3a3f98c9b4961df; cookie17=UUkO1Kv%2FeCMlYQ%3D%3D; dnk=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; skt=2f3d81f56f5c16b0; munb=2100521411; cookie2=1b5bc95e650d265b1d8159b38b544c77; uc4=id4=0%40U2uCu3NZb8FJne85RaKSrX7%2FPDS8&nk4=0%40sVYXnVU9W%2B32DLENh4iu5qxpUlckKQ%3D%3D; tracknick=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; _cc_=VFC%2FuZ9ajQ%3D%3D; ti=1568860058617%40taobao_android_9.25.0; sg=21d; _l_g_=Ug%3D%3D; _nk_=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; cookie1=AiBidlwPGZHvoyjWBBi2DYD0Yaidkhe6VY8HPgbAEgU%3D; _tb_token_=ee4b8b383bde; sgcookie=W100z3Cb7qXZSW%2FJp98oc1goxkI6uHOzvW7PndgX0mkI8t%2FOiKraPhPFdoK6pfwGOCy0yTfOMbZakUDhOfEWNXN2rMOuvQxkiyjK2%2F3MzNg7ZOU%3D; imewweoriw=3%2FqcKUC8ML9xucTzN5%2B2W6LA9%2BxNQdXdHyjfcgTjBFU%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuUTJFJmnP9vVxdsYhSE6jeU%3D; _w_tb_nick=%E5%B0%8F%E7%B3%AF%E5%9B%A2%E5%AD%90712; ockeqeudmj=r4pchfM%3D; cna=FAwyGVKFSywCAXPFJohibZcS; isg=AhUVQH1-2e2Nnv0Byz_8iFumLxPPEskkH_fZ-pe60Qzb7jXgX2LZ9COuysgn',
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
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "appKey": "21646297",
            "ext": f"{ctime.millis}",
            "from": "小糯团子712",
            "id": "2100521411",
            "namespace": 1,
            "role": 3,
            "sdkVersion": "0.3.0",
            "tag": "tb",
            "timestamp": ctime.millis,
            "topic": "a2d99dae-8e0b-4879-857b-e824f016c351",
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
            'x-sid': '1b5bc95e650d265b1d8159b38b544c77',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622733009879',
            'x-uid': '2100521411',
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
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; unb=2100521411; sn=; uc3=vt3=F8dCuw76qoBME0VRJPk%3D&id2=UUkO1Kv%2FeCMlYQ%3D%3D&nk2=sym3Yze86A%2FjQSg%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; uc1=cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie14=Uoe2z%2BTLhW13lw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false; csg=bae1b678; lgc=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; t=a2b917c50bd04e33a3a3f98c9b4961df; cookie17=UUkO1Kv%2FeCMlYQ%3D%3D; dnk=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; skt=2f3d81f56f5c16b0; munb=2100521411; cookie2=1b5bc95e650d265b1d8159b38b544c77; uc4=id4=0%40U2uCu3NZb8FJne85RaKSrX7%2FPDS8&nk4=0%40sVYXnVU9W%2B32DLENh4iu5qxpUlckKQ%3D%3D; tracknick=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; _cc_=VFC%2FuZ9ajQ%3D%3D; ti=1568860058617%40taobao_android_9.25.0; sg=21d; _l_g_=Ug%3D%3D; _nk_=%5Cu5C0F%5Cu7CEF%5Cu56E2%5Cu5B50712; cookie1=AiBidlwPGZHvoyjWBBi2DYD0Yaidkhe6VY8HPgbAEgU%3D; _tb_token_=ee4b8b383bde; sgcookie=W100z3Cb7qXZSW%2FJp98oc1goxkI6uHOzvW7PndgX0mkI8t%2FOiKraPhPFdoK6pfwGOCy0yTfOMbZakUDhOfEWNXN2rMOuvQxkiyjK2%2F3MzNg7ZOU%3D; imewweoriw=3%2FqcKUC8ML9xucTzN5%2B2W6LA9%2BxNQdXdHyjfcgTjBFU%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuUTJFJmnP9vVxdsYhSE6jeU%3D; _w_tb_nick=%E5%B0%8F%E7%B3%AF%E5%9B%A2%E5%AD%90712; ockeqeudmj=r4pchfM%3D; cna=FAwyGVKFSywCAXPFJohibZcS; isg=AhUVQH1-2e2Nnv0Byz_8iFumLxPPEskkH_fZ-pe60Qzb7jXgX2LZ9COuysgn',
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
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "anchorId": "790956988",
            "liveEventsJson": "[{\"accountId\":\"790956988\",\"action\":\"enter\",\"count\":1,\"extendJson\":\"{\\\"entrySource\\\":\\\"null\\\",\\\"fansLevel\\\":\\\"0\\\",\\\"liveSource\\\":\\\"null\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"sjsdItemId\\\":\\\"null\\\",\\\"timeMovingItemId\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"0\\\"}\",\"feedId\":\"311734092779\",\"scene\":\"taobaolive\",\"timestamp\":\"%s\",\"type\":\"0\"}]" % ctime.millis,
            "liveId": "311734092779"
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
