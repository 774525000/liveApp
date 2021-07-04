from spider import upload
from typing import NamedTuple, Union
from random import choices


def rand_str():
    rand_arr = [*[str(item) for item in range(10)], *[chr(item) for item in range(97, 123)],
                *[chr(item) for item in range(65, 91)]]
    res = choices(rand_arr, k=32)
    return ''.join(res)


class Params(NamedTuple):
    user_id: str
    user_name: str
    u_mid: str
    imei: str
    open_id: str
    live_id: str
    stay_time: Union[int, float]


@upload(file_name='live.txt')
def live_upload(data, params: Params):
    return data.format(
        user_id=params.user_id,
        user_name=params.user_name,
        umid=params.u_mid,
        imei=params.imei,
        open_id=params.open_id,
        live_id=params.live_id,
        stay_time=params.stay_time
    )
