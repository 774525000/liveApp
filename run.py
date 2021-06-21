import httpx, requests
from requests_toolbelt import MultipartEncoder

if __name__ == '__main__':
    url = 'https://passport.taobao.com/iv/identity/verify_rs.do'

    data = [
        ('params',
         '{"endpoint":{"mode":"h5","standard":true,"osVersion":"9.9.9","protocolVersion":"3.0","ultronage":true},"linkage":{"common":{"compress":true,"submitParams":"^^$$87BEDFBFF67242B37E1C9FB92098A2A2{$_$}H4sIAAAAAAAAAJ2QQUvEMBCF/0vONXhYod2TKIKCC4K6FxGZJrO7o2mmpJNiXfrfnVaXBQ8iHt8X3subtzfnMrRolsZxYyFQDTVY6IQT2jaxsONgc5DEEbZoG/YY7OOsbym+KbuDBE1niimh4fgtl3sD3RDdin0OqPoe5cmQX2OizfBSLs6qUj39LC+yCMcZVua5MDV9XOpH2kobWbejCFaAa2C1UGyz/Cu21bY3XlPL02phvvTD0Cqg/sSjAIUjxR+4cxghESv2uAGdZIK0jSA54Qra6eTDmK/Qg81CwV5Dt5sex7EwzVz66h1dFjzu9Ivp4FnrDv5PjvETPuvTy9IBAAA=","validateParams":"^^$$FE424B522230CAC4956117C946ABC703{$_$}H4sIAAAAAAAAAI2NMQrCQBBF7zK1zAFS2QgWCjba/2wGjc5mlt1ZUULu7iLE2vK/z+PNtPV3EuooWGTo2KMHo7hl4ZTNLZhyVc824SocbRDl83cfxunR2AkZsdCG2ldVdi8J1Vfazb/AHU9w9VF5j3I7ItGyOpcWHv4ylg8/RHe2sQAAAA=="},"signature":"99554A1A657CD4B8AF884684C3C8B739"},"data":{"idVerify_84598":{"scriptKey":"IdVerify_84598","submit":true,"id":"84598","position":"body","tag":"idVerify","fields":{"cardType":"1","tips":"","value":"3010"},"type":"idVerify","status":"normal"},"verifyButton_84599":{"scriptKey":"VerifyButton_84599","submit":true,"id":"84599","position":"body","tag":"verifyButton","fields":{"disabled":true,"text":"下一步"},"type":"verifyButton","status":"normal"}},"hierarchy":{"structure":{"root_84596":["instruction_84597","idVerify_84598","verifyButton_84599","otherVerify_92945"]}}}'),
        ('type', '1'),
        ('tag', '1'),
        ('htoken', 'fHIkwECe1JjSuiPBAfYR0Xs5lC5qd4oWEbO9c006OE5P9q2px36jVIVa8KKuISKZks-6F4MK-_vJYuh0WRQ74g'),
        ('bx-ua',
         '212!NKWWZqcVWW5QoagQUWhQEY0ITO4wWWW6E9hZvA9TW1Lw/PUwv+niE5iITO4wxBMTqSA+vFfiw55uT2jkxWWpWpl9pSe8v3IexWQbpGNiS3/nEM1WO+zR/ci9js31A/RWpwR8yZauQtrIDrgm97IZpNC6LOyJo8h5Em/MYYiixvK/HB8K5tlMS4+HCt4Cjdx3Z6Nq2Y/V7NtzHQ5z7/ypmr+9Ro7OKGi75Lm8Vq3aCbSSDdLUnyoP2bH3d8evsLCKNjiMr050fUCQLDygUv6BpZ42TzV6siab0bBu2uWR52BN1yQp5ZQLlu4RiMS2PhmBkG8lLcF5Wq5uiKrSvMuq8WiCpHmpGFZ0i6BMJPoJSF7dcbo2nLUpBrWyBNx5HUs49T7Qf3tB/1bgbbqnaoiJ75t8k/vaWeB36wUpWxz6wIzArGQRzdkoEb17PRmuS/e6RCtEpTMKbyL9zhaJFSn4Qudxp/W8iGEmrI5CmTLLwQ/a1YPGITqOxH9IIQU3QGM6JJDJjQk78fzKTGGgzlmbAOafhcYqsEMG8JvujpRmKP205bsXyx5CxJcEzNVNrs2RepPIiKhhG34lNJCocI9+ToDpkxXXN6veQQ5pz3pnO0bneEaSCBiSVJxoPPX5KGREbaWkjxweZeBC3Bed91UWU4S2fKlk2bFfVx/rAD8r7gtFclQH2OsRV+RQ/sq657kF8mKtiVEpFrureQO38ZJzSTDXK41dp/SgplOsqkI+JUb0MpUm0iP+NS2I/gaHL49JmnX2ZcDyWAuu0IUghOfQSyDKmM/HBvpm2RHhdddBBLBP4dedzTj5Pi/HGwH9SnQM4aNnPaj31jDZqU/6d0r7CBuD6l52o4vsYNPikFkMZpaAz/+ulxCdNAWp0SNDxxPnp02HEzlGK1+7lXbK4Ca3+MdY67oTesfOa2hyk24kabyAyMbfjmoAoM8TiF+LqK6Lu2QOaEHmif0uFF3tmJAHDfWpp8KKLkvNjvz94lgh42LD3phhvfEkPnEN2QttfPpE6HbUr7NEzY320qUaBVcgvo7vyj9N6iO1fF3LGqDvPFTlR5bE5Cn+ZEXsVJXutuRGEvL+xWRjanqKps4sqfu0T78XBpuDdKspJz2S7Rne7Eo0voTbMMeFrb83o5hbfYlXE/+XTUUlN+ZxsMkekTxk+710KnAaXd0yCFG6k0nfZCJTPv55nM58hPN0SdXmJknPCksHwT8emc3L5Bl='),
        ('bx-umidtoken', 'T2gAZ1UbKN9E3DTuhV9AGmrND1Gx1a7r2ZkgnsH2-cQLbbt-x6z2pbLjNMt4de4NCBY=')
    ]

    params = {
        '_bx-v': '2.0.40'
    }

    encoder_data = MultipartEncoder(fields=data, boundary='----WebKitFormBoundaryAzsSMS4aKN5JBtRo')

    headers = {
        'Origin': 'https://passport.taobao.com',
        'Cookie': 'xlly=1; thw=cn; JSESSIONID=KP966C71-WK3RXSP5ZXEHTT4DAYKO1-TC21R1QK-7RT; ivActionType=sdk_smslogin_check; tmp0=CjeTRP%2FMhsEzWYPp%2FDx4GJor1VfgnCD8KQLH90Yt0w3695Ilrt8daEvg72t74WvRyHuaxaN8NbvqYKNOpvaCbbVeYgTYjCYHVPWyxYKmKeLPhs3HwntzfuU%2BDn7D8IYc8xmL1ROere1FCYnULhOOfQ%3D%3D; siv20=nlRyzPBC%2B0Zkqp0uOcKJKfdSH0OUYRDjBTyFjU7tsmuWvw68aoFN2BHgDZ9NpQtrszivPz5rIL0kXdg53XuIfQ9iq4nfKza7tRLXdHIGoH36PCpO2E82BSGBJQwwBZ2Ne0oyhr%2BeGTVQzzc3KohkFA%3D%3D; _bl_uid=k5k9FqhC1L7q3XydCk4y1yj881FC; cna=W/tSGQRvphQCAXPDi8l3FPqC; tfstk=cIMhBV1ueJPL9rViGpwIx5quPGROax848flsQYw4DyRzsQkaYsDN__p9oU4Djdf5.; l=eBxeGxsrjeEJgr6UBOfChurza7zeICOJMuPzaNbMiOCPOA1p5syfW6OpMy89CnNRn6bB538XM_XWBP8KEyUHhbSe-H8V1eJnFpdC.; isg=BBsbL6hi_24VxwOa8VnCrYVHoX2F8C_ypTWHJA1Y9Zox7D_OkcA6QshqggpEBIfq',
        'f-refer': 'wv_h5',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; Nexus 5X Build/OPM7.181105.004) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.115 Mobile Safari/537.36 AliApp(TB/9.25.0) UCBS/2.11.1.1 TTID/1568860058617@taobao_android_9.25.0 WindVane/8.5.0',
        'Referer': 'https://passport.taobao.com/iv/h5/identity_verify_as.htm?tag=1&lang=zh_CN&htoken=fHIkwECe1JjSuiPBAfYR0Xs5lC5qd4oWEbO9c006OE5P9q2px36jVIVa8KKuISKZks-6F4MK-_vJYuh0WRQ74g',
        'x-c-traceid': 'YKnJdlCwF6oDACfhFIu95LNr16239853961801366e3ba2',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-CN;q=0.9,en-US;q=0.8',
        'Content-Type': encoder_data.content_type,
        'Host': 'passport.taobao.com',
        'Connection': 'Keep-Alive'
    }

    proxies = {
        'http': 'http://192.168.0.204:8888',
        'https': 'http://192.168.0.204:8888'
    }
    res = requests.post(url, data=encoder_data, params=params, headers=headers, proxies=proxies,
                        verify='./FiddlerRoot.pem')
    print(res.text)
