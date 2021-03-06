from spider import Spider, Api, get_unix
from utils import get_lower_num, get_lower_upper_num


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
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 6P)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "new_device": "true",
            "c4": "",
            "c5": "unknown",
            "c6": get_lower_num(),
            "device_global_id": get_lower_upper_num(),
            "c0": "google",
            "c1": "Nexus 6P"
        }


class SmsSend(Spider):
    def __init__(self, mobile, params):
        self.is_get = False
        ctime = get_unix()

        self.api = Api('mtop.taobao.mloginservice.smssend', '1.0')

        device_id = params['data']['device_id']

        self.headers = {
            'x-sgext': 'JAEHZhrj3CTTCrdr305aq2Y2VjZWNUU0VzJUNkU1XyRFNlA1VDFUMFU+Ug==',
            'x-social-attr': '2',
            'x-sign': 'azYBCM003xAAJ9TN7IPd2AXjYKSFF9TH0OKfsdNZG+6FgCTOa6NnAeGcpOBID2R9uVC2381yUOKfncDDhPaQc3WDfVfU19TH1NfUx9',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622628800269',
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'login_sdk_version': '4.5.8.45',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_LT01l7D1VCuBz9uhmsD3y/cKbThKgXIDNw//IMIwpmTztnZ5mh4Q1oV4mUoXuD7yi5oDZQTuZXACDKQnGguaw2AHe9vGILL+GTRokPCQyHetJiGXek2A9yCjSczOlB0+TDpXi3W9govWwXRfT1RmNuZtYqCwEDBetz261euNFco=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'thw=cn',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YLdUQZXeZo0DAGVXLtLwfk0R16226290391920347131521',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210602175402851',
            'x-umt': 'PSoAxD5LPLrbIwJ5zLNf9fOAIcIeRX8a',
            'x-utdid': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'c-launch-info': '1,0,1622629039192,1622627388378,2',
            'x-appkey': '21646297',
            'x-page-url': 'http://m.taobao.com/index.htm',
            'x-page-name': 'com.ali.user.mobile.login.ui.UserLoginActivity',
            'x-devid': device_id,
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 6P)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "ext": "{\"apiReferer\":\"{\\\"eventName\\\":\\\"autoLoginToken=null|trySdkLogin\\\"}\",\"apiVersion\":\"2.0\",\"deviceName\":\"Nexus 6P\",\"sdkTraceId\":\"smsLogin_YLdUQZXeZo0DAGVXLtLwfk0R_1622629039_pagelogin_YLdUQZXeZo0DAGVXLtLwfk0R1622629019\"}",
            "loginInfo": "{\"appName\":\"21646297\",\"appVersion\":\"android_9.25.0\",\"codeLength\":\"4\",\"countryCode\":\"CN\",\"deviceId\":\"%s\",\"deviceName\":\"google(Nexus 6P)\",\"locale\":\"zh_CN\",\"loginId\":\"%s\",\"loginType\":\"taobao\",\"phoneCode\":\"86\",\"sdkVersion\":\"android_4.5.8.45\",\"site\":0,\"t\":1622629039164,\"ttid\":\"1568860058617@taobao_android_9.25.0\",\"useAcitonType\":true,\"useDeviceToken\":true,\"utdid\":\"YLdUQZXeZo0DAGVXLtLwfk0R\"}" % (
                device_id, mobile),
            "riskControlInfo": "{\"apdId\":\"a424ae99db0045f9fcbd02f0129cd2d181c0cd94\",\"t\":\"1622629039165\",\"umidToken\":\"FH8Am\/ZLPGNVtwJ5zIsLptl2IYGbWEJU\",\"wua\":\"FKr2_yPjj7BH28qEwhVU0sekXjuIAlws0jcKW+GrAk0j05hDvOd1fz0GdA662UxR4uGzIgsLQxRJz43a0JexCGWyw85GH8byl7rJdferQIw36Po3lQRolx8KHhNVeaZnChMpg7NT840+I6Zmz5P43ylHkiMU+QP3qHt1JAhJxnM5NmtzuBjwKM989xBhc9qOM44gZkQytCzMPx2wIhgExRQsrC4+MAGW8zDMMMx8MHqfYi1RsPfZw5exlhNrzqf4Z4MiqwaoLRhhf+iVlR7izfizzDG4Va6YuVFDHXMLssrS17OCQwcUeIFOxf+lg2z\/Am2SDx8kH+o\/Tn7QfhCxxQner9KIzJXbe5dMEJTxwwlYgkAEab1MchbOukAABcFGyR0wSnlN6IcdWBVknTr1JusMH3e4UPpAjOhhDf23fJYU8WgnWkSetro+VfAyOE5s9ZLkM\"}"}


class SmsLogin(Spider):
    def __init__(self, params1, code, mobile, params2):
        ctime = get_unix()
        self.is_get = False

        self.api = Api('mtop.taobao.mloginservice.smslogin', '1.0')

        sms_sid = params2['data']['returnValue']['extMap']['smsSid']

        device_id = params1['data']['device_id']

        self.headers = {
            'x-sgext': 'JAE2fgLSxBXLO69ax39Cmn4HTgdOBF0FTwNMB10FThVdB0gETABMAU0PSg==',
            'x-social-attr': '2',
            'x-sign': 'azYBCM003xAALD+5mxLttI/kF7FuXD+8O5l0yjgi8JVu+8+1gNiMegrnT5ujdI8GUitdpCYJu5l05iu4b417CJ74liw/rD+8P6w/vD',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622628800269',
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-nq': 'WIFI',
            'login_sdk_version': '4.5.8.45',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_CCq5FJWTK3AXg5krwovIv8vE5zlCG3lSJ7/bkwf7MBOkl/0U1y4JA3GuBuDC4MbgvwZ7zdDxDJfRTf9ykkj4/iqwzfixmMhCQABg3kY9czg1VJ7MPLCS/3LXBt96Che7w6tB310LNmcfFDRq5/AvTBkZW7L4PmX4R3HwxcuhEAM=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'thw=cn',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YLdUQZXeZo0DAGVXLtLwfk0R16226298202280350131521',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210602175402851',
            'x-umt': 'PSoAxD5LPLrbIwJ5zLNf9fOAIcIeRX8a',
            'x-utdid': 'YLdUQZXeZo0DAGVXLtLwfk0R',
            'c-launch-info': '1,0,1622629820228,1622627388378,2',
            'x-appkey': '21646297',
            'x-page-url': 'http://m.taobao.com/index.htm',
            'x-page-name': 'com.ali.user.mobile.login.ui.UserLoginActivity',
            'x-devid': device_id,
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 6P)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "ext": "{\"apiReferer\":\"{\\\"eventName\\\":\\\"autoLoginToken=null|trySdkLogin\\\"}\",\"apiVersion\":\"2.0\",\"deviceName\":\"Nexus 6P\",\"sdkTraceId\":\"smsLogin_YLdUQZXeZo0DAGVXLtLwfk0R_1622629039_pagelogin_YLdUQZXeZo0DAGVXLtLwfk0R1622629019\"}",
            "loginInfo": "{\"appName\":\"21646297\",\"appVersion\":\"android_9.25.0\",\"countryCode\":\"CN\",\"deviceId\":\"%s\",\"deviceName\":\"google(Nexus 6P)\",\"locale\":\"zh_CN\",\"loginId\":\"%s\",\"loginType\":\"taobao\",\"phoneCode\":\"86\",\"sdkVersion\":\"android_4.5.8.45\",\"site\":0,\"smsCode\":\"%s\",\"smsSid\":\"%s\",\"t\":1622629820198,\"ttid\":\"1568860058617@taobao_android_9.25.0\",\"useAcitonType\":true,\"useDeviceToken\":true,\"utdid\":\"YLdUQZXeZo0DAGVXLtLwfk0R\"}" % (
                device_id, mobile, code, sms_sid),
            "riskControlInfo": "{\"apdId\":\"a424ae99db0045f9fcbd02f0129cd2d181c0cd94\",\"t\":\"1622629820198\",\"umidToken\":\"FH8Am\/ZLPGNVtwJ5zIsLptl2IYGbWEJU\",\"wua\":\"FKr2_nb8lbVdoWWKrdwd0kSKZdpK9ehuMTs1FnJG7gVMzg+jtMkVxfP2s6hjmKr23RSqsfMTQa4UDExSLDnYXwCfVdllCtImOR5UUPUhD41kPg3Kr+Xbf44FNIhYYtu1CpEQxeTZFWy6kvAchfo7bKUrDZp7UzfsPoi4Fk6ttwQcLxW6uHDiMvzzWTQdrSEVkieGrF2gVE\/M6314C5ayb33N5FbM0B0fIR2BuKMzEEpsobTYD+WiIRV2zkmZ6EdNv6K8lPo9I9WS7gtocvKGVqSPK9gx0cN7yq8KEEA1x6K1GA+Al7iEFYcoF3amfoDoRFy1oCRwp19SBuqX2LZAHmifnbroDxDr4+Ks3690Nj2vB0DRalnX4lGQtX7s71dFADz38ljhHJ37JmppwlPRIiiYg9oS1vIF2UsNCNfuygbkHRDvwKfMbz9dNv30K9wqFK+6L\"}"}


class Login(Spider):
    """
    ????????????
    """
    def __init__(self):
        ctime = get_unix()
        self.is_get = False

        self.api = Api('com.taobao.mtop.mloginservice.login', '1.0')

        self.headers = {
            'x-sgext': 'JAEEwx6POPZ2CRJoek3/qMM18zXzNeA88Tf7J/Iy8TfgJ/Iy8TfzN/A9+jA=',
            'x-social-attr': '3',
            'x-sign': 'azYBCM003xAAJVcVwSM1PXH5EuZCZTcVUJnNg1CLmDwOoJcVUoHk11JfpzLJHOO2nNP8j0TSH/acT0MRByQTofZR/oVXBVcVVwVXFV',
            'x-sid': '2775809838c2887a187b91f506e8c92d',
            'A-SLIDER-Q': 'appKey=21646297&ver=1622981502612',
            'x-uid': '2209572427031',
            'x-nettype': 'WIFI',
            'x-pv': '6.3',
            'x-disastergrd': '',
            'x-nq': 'WIFI',
            'login_sdk_version': '4.5.8.45',
            'x-region-channel': 'CN',
            'x-features': '27',
            'x-app-conf-v': '0',
            'x-mini-wua': 'HHnB_3ZU1q09/ZTcNnQRt5JQyZOtlYBTiPszx1Ewud6VcgDNgh7vvZh4OwyuwTkj90gjo2LVnTGi1WTiRJ4JKRmFKSsms6fBZ01lRtV74vMmI/MOG9E8dwn67GNOvTEcnM4+pSfhT5tdRAN6ejiyUpozwIaLVrKB4vx22WWieF7hd+oM=',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Length': '2232',
            'x-t': f'{ctime.seconds}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'thw=cn; tfstk=clRVBVxEQszNaV1sps1alLhHblqACjBl3R7fnLuz470x3b0FjE5m7lQSD4jNfRhOn; l=eBPkPikcjnnrHtT-BO5ZPurza7SF2IRZhCVzaNbMiInca6Lh_FM3FNCCPoFX8dtYwt1FbetylIClFdLHR3sdvxDDBUy83k4i32C..; _m_h5_tk=99e0959ecd066654051d0c1a4c054abd_1622800022257; _m_h5_tk_enc=8dfa8559ab5b9406b94066194c9af68b; xlly=1; unb=2209572427031; uc3=vt3=F8dCuw7+gb+rbuIvHeY=&id2=UUphw2BCaFXrTatuAA==&nk2=F5RMGoXjyRtiUrA=&lg2=VT5L2FSpMGV7TQ==; uc1=cookie14=Uoe2zsmzzvtzyg==&cookie15=WqG3DMC9VAQiUQ==&cookie21=VFC/uZ9ainBZ&existShop=false; csg=7ac735ed; lgc=tb931554566; t=46a9cbd2288b23388130ed713a76b739; cookie17=UUphw2BCaFXrTatuAA==; dnk=tb931554566; skt=1a5c938a899c6db5; munb=2209572427031; cookie2=2775809838c2887a187b91f506e8c92d; uc4=id4=0@U2grGN9Axww7kF+A9HhylLSlKE12GYeX&nk4=0@FY4HX7dO8Wd8xUGIADymp6EtntfFow==; tracknick=tb931554566; _cc_=Vq8l+KCLiw==; sg=61b; _l_g_=Ug==; _nk_=tb931554566; cookie1=AiAzS86U8AyQM+t18C+d5FT5KmB2ZSwxil9tZ5khPIU=; _tb_token_=ee561655b6eef; sgcookie=W100ZXpWS19OYAioKT9B3UxWHPQamMvlReMQ66KcKam955HUrL5TuvOfJtCEyjiVMJNf5BOJf76HGSipSBIy4FPVLg93mJCgs/mvj6bfJuu0NL8=; imewweoriw=3HOahQlaA1sKWUlyf+smbmou09pzC0swSeFP1vhdIEg=; WAPFDFDTGFG=+4cMKKP+8PI+KK8XUFmnFqlIaVJQJw==; _w_tb_nick=tb931554566; ockeqeudmj=j+0GVTk=; cna=FAwyGVKFSywCAXPFJohibZcS; isg=BJ6eJFyNcnSpnaYEtMKHZRzj5DbgX2LZeBJiP0gnCuHcaz5FsO-y6cQKZzFFolrx',
            'x-bx-version': '6.5.27',
            'f-refer': 'mtop',
            'x-extdata': 'openappkey=DEFAULT_AUTH',
            'x-ttid': '1568860058617@taobao_android_9.25.0',
            'x-app-ver': '9.25.0',
            'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr1623044583880274018238',
            'x-location': '120.162405,30.184987',
            'a-orange-dq': 'appKey=21646297&appVersion=9.25.0&clientAppIndexVersion=1120210607131700837',
            'x-umt': 'm1wAAFlLPCBUrwJ54JtKPLxquaE8dI48',
            'x-utdid': 'YKnJdlCwF6oDACfhFIu95LNr',
            'c-launch-info': '3,0,1623044583880,1623033985470,3',
            'x-appkey': '21646297',
            'x-page-url': 'http://m.taobao.com/go/mytaobao/newsettings',
            'x-page-name': 'com.ali.user.mobile.login.ui.UserLoginActivity',
            'x-devid': 'Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6',
            'user-agent': 'MTOPSDK/3.1.1.7 (Android;8.1.0;LGE;Nexus 5X)',
            'Host': 'guide-acs.m.taobao.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }

        self.data = {
            "ext": "{\"apiReferer\":\"{\\\"eventName\\\":\\\"SESSION_INVALID\\\"}\",\"apiVersion\":\"2.0\",\"deviceName\":\"Nexus 5X\",\"scene\":\"recommendLogin\",\"sdkTraceId\":\"pwdLogin_YKnJdlCwF6oDACfhFIu95LNr_1623044583_pagelogin_YKnJdlCwF6oDACfhFIu95LNr1623044489\"}",
            "loginInfo": "{\"appName\":\"21646297\",\"appVersion\":\"android_9.25.0\",\"deviceId\":\"Atzi2cGlhQSAlW_BJjJULENjeY88Cyak5-o8mmUXCIP6\",\"deviceName\":\"google(Nexus 5X)\",\"locale\":\"zh_CN\",\"loginId\":\"18966485271\",\"loginType\":\"taobao\",\"password\":\"SEzzvkrosamylS9bF00R0uk7TuurROLsb8khwDkog046NcJzGk4VcI6mCYIMhqaBJI6NueDETnJZR\/+uHrBzzwkkXVAS1aHh+qNZS8hfLZxXW5zTMqkRcrmzi9+3B5aukvy82e3a0odSyeOB1A+8GFwCRqXLAT9QFBcdike\/vBU=\",\"pwdEncrypted\":true,\"sdkVersion\":\"android_4.5.8.45\",\"site\":0,\"t\":1623044583851,\"ttid\":\"1568860058617@taobao_android_9.25.0\",\"useAcitonType\":true,\"useDeviceToken\":true,\"utdid\":\"YKnJdlCwF6oDACfhFIu95LNr\"}",
            "riskControlInfo": "{\"apdId\":\"eYOIk2CLcACx6FGpVkocCUAAjj4O0SzSzALdEjmkxcsMhggERpFZx+BM\",\"t\":\"1623044583851\",\"umidToken\":\"m1wAAFlLPCBUrwJ54JtKPLxquaE8dI48\",\"wua\":\"FKr2_g+nKIisDKqZfC1T1k\/SO+OsyB3mcXJDhK8Mj7xjABoDVIaSFPaLhMLGdjxi+XLS4E8bt5Lt93xnij0O8lQs9LSFMt9v3Dyfgbyig2hwmakUtxAJYp\/QwzFjTt89YxMJ2kyHXZ1XPHreFxafLqkLRwF8CPIZMCeZHU4M4NZY+S6\/CPx8XA2J\/NKN+w63+h65JUF7KSmj3YlMbkIBrpeo9XUD8vEAK1K+EoO4jq6auZbYptF+3TEoZHeVciDlYcCL\/xUTgoMdEAoL2CPSZsZ49QSgC7EeWlTEFiXVThpkSD8SaYsxiQyvdmzd0jHO\/wiO2nfdYVEZIk4ff83HPzJ5jNJ5l2lmwYDPXwQUv6YN6MOOMbf6A67T87cqoWQr+3hEnXpfP20ZLloaaOARkG9vAyBhCbNwG2mvO9kd\/POK3n2jTL\/Ct71IdL+QM+MIJLRsFwOpf+\/usTsUoZOqf+2LIxg==\"}"
        }
