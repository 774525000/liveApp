from ._login import NewDevice, SmsSend, SmsLogin
from app import task


@task.add_task('login')
async def auto_login():
    new_device = NewDevice()
    params1 = await new_device()
    print(params1)

    mobile = input('请输入手机号：')
    mobile = mobile.strip()

    sms = SmsSend(mobile, params1)
    params2 = await sms()
    print(params2)
    code = input('请输入验证码：')
    code = code.strip()

    smg_login = SmsLogin(params1, code, mobile, params2)
    params3 = await smg_login()
    print(params3)
