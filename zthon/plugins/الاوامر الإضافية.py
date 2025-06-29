from ..core.managers import edit_or_reply
from . import zedub

# t.me/senzir1
ZelzalDV_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝐑𝐄𝐅𝐙 - التحديثات الجديدة ](t.me/def_Zoka) 𓆪\n\n"
    "⪼تم اضافه امر .بعصه\n"
    "⪼تم اضافه امر .شطان\n"
    "⪼تم اضافه امر .انطق\n"
    "⪼سيتم اضافه الاوامر الاخرى قريبا\n"
    "\n𓆩 [𐇮 𝙎𓏺𝞝𝙉𝙕𝙄𝙍 الهہـيـٖ͡ـ͢ـبـه 𐇮](t.me/senzir1) 𓆪"
)

@zedub.zed_cmd(pattern="م30")
async def cmd_30(event):
    await edit_or_reply(event, ZelzalDV_cmd)


# t.me/senzir1
ZelzalDV_cmd_2 = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝐑𝐄𝐅𝐙 - اوامر الانتحال ](t.me/def_Zoka) 𓆪\n\n"
    "⪼ .انتحال\n"
    "⪼لاعاده حسابك كمان كان ارسل  .اعاده\n"
    "\n𓆩 [𐇮 𝙎𓏺𝞝𝙉𝙕𝙄𝙍 الهہـيـٖ͡ـ͢ـبـه 𐇮](t.me/senzir1) 𓆪"
)

@zedub.zed_cmd(pattern="م31")
async def cmd_31(event):
    await edit_or_reply(event, ZelzalDV_cmd_2)
    
