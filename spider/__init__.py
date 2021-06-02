from ._utils import Api, dumps, merge_dict, get_unix, encode_headers
import httpx


class Spider:
    headers: dict = {}
    data: dict = {}
    data_dumps: str = ''
    api: Api = None
    is_get = True
    client: httpx.AsyncClient = None

    async def run(self):
        self.data_dumps = dumps(self.data)
        headers = await self.get_headers_params()
        return await self.send_request(headers)

    async def send_request(self, headers):
        params = {
            'data': self.data_dumps
        }

        headers = encode_headers(headers)

        url = f'http://guide-acs.m.taobao.com/gw/{self.api.api}/{self.api.v}/'
        if self.is_get is True:
            res = await Spider.client.get(url, params=params, headers=headers)
            return res.json()
        else:
            res = await Spider.client.post(url, data=params, headers=headers)
            return res.json()

    async def get_headers_params(self):
        url = 'http://192.168.0.141:10086/sign'

        data = {
            **self.get_base_headers(self.headers),
            'data': self.data_dumps,
            'v': self.api.v,
            'api': self.api.api
        }

        res = await Spider.client.get(url, params=data)
        params = res.json()
        return merge_dict(params, self.headers)

    @staticmethod
    def get_base_headers(headers):
        location: str = headers['x-location'] if headers.get('x-location') else ','
        loc_ = location.split(',')

        return {
            'ttid': headers['x-ttid'],
            'utdid': headers['x-utdid'],
            'deviceId': headers.get('x-devid', ''),
            'xFeatures': headers['x-features'],
            't': headers['x-t'],
            'appKey': headers['x-appkey'],
            'lng': loc_[0],
            'lat': loc_[1],
            'pageName': headers.get('x-page-name', ''),
            'pageId': headers.get('x-page-url', ''),
            'uid': headers.get('x-uid', ''),
            'sid': headers.get('x-sid', ''),
            'useWua': 'false',
            'requestID': 'r_79',
            'extdata': headers['x-extdata']
        }

    async def __call__(self, *args, **kwargs):
        return await self.run()

    async def __aenter__(self):
        Spider.client = httpx.AsyncClient()
        return Spider.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await Spider.client.aclose()
