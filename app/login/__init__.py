from .login import NewDevice


async def auto_login():
    new_device = NewDevice()
    res = await new_device()
    print(res)
