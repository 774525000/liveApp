from spider import upload
from ._utils import Params


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


@upload(file_name='keep_live.txt')
def keep_live_upload(data, params: Params):
    return data.format(
        user_id=params.user_id,
        user_name=params.user_name,
        umid=params.u_mid,
        imei=params.imei,
        open_id=params.open_id,
        live_id=params.live_id,
        stay_time=params.stay_time
    )
