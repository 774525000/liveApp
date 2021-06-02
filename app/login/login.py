from spider import Spider, Api, get_unix


class NewDevice(Spider):
    def __init__(self):
        ctime = get_unix()

        self.api = Api('mtop.sys.newdeviceid', '4.0')

        self.headers = {
            'x-sgext': 'JAHQTTE09/P43Zy89JlxfE3hfeF94m7jfOV/4W7ibvN85n/ie+J643Tk',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-social-attr': '2',
            'x-sign': 'azYBCM003xAAJcjXUfgrwvHmkMAo9cjVzPCDo89LB/yb5OLdcU69mbBxlcIlfcHR1izstwbVJtFzj9zRmOSMYWmRYUXIxcjVyMXI1c',
            'x-c-traceid': 'YLdUQZXeZo0DAGVXLtLwfk0R16226273941350003131521',
            'x-pv': '6.3',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-umt': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'x-mini-wua': 'HHnB_x5hqxRKGfHn+skJIFKPunz5B5XiF+uyZjBIxjdYxNQ0=',
            'x-utdid': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'c-launch-info': '1,0,1622627394133,1622627388378,0',
            'x-appkey': '21646297',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cache-control': 'no-cache',
            'x-t': f'{ctime.seconds}',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "new_device": "true",
            "c4": "",
            "c5": "unknown",
            "c6": "ea81cf6e1418df54",
            "device_global_id": "YLdUQZXeZo0DAGVXLtLwfk0R",
            "c0": "google",
            "c1": "Nexus 5X"
        }
