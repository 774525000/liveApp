from ._login import NewDevice, SmsSend, SmsLogin
from app import task


@task.add_task('login')
async def auto_login():
    new_device = NewDevice()
    res = await new_device()

    mobile = input('请输入手机号：')
    mobile = mobile.strip()

    sms = SmsSend(mobile, res)
    res = await sms()
    code = input('请输入验证码：')
    code = code.strip()

    smg_login = SmsLogin(code, mobile, res)
    res = await smg_login()
    print(res)