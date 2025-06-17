import html
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from ..Config import Config
from . import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, zedub, edit_delete, get_user_from_event
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = Config.DEFAULT_BIO or "- ‏وحدي أضيء، وحدي أنطفئ انا قمري و كُل نجومي..🤍"
ANTHAL = gvarstatus("ANTHAL") or "(إعـادة الحـسـاب|اعادة|اعاده)"

async def update_profile(event, replied_user):
    user_id = replied_user.id
    profile_pic_path = await event.client.download_profile_photo(user_id, file=Config.TEMP_DIR)
    
    first_name = html.escape(replied_user.first_name or "")
    first_name = first_name.replace("\u2060", "")
    
    last_name = html.escape(replied_user.last_name) if replied_user.last_name else "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    last_name = last_name.replace("\u2060", "")
    
    full_user = await event.client(GetFullUserRequest(user_id))
    bio = full_user.full_user.about or ""

    # تحديث الاسم والبايو
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name, last_name=last_name, about=bio))

    try:
        uploaded = await event.client.upload_file(profile_pic_path)
        await event.client(UploadProfilePhotoRequest(file=uploaded))
    except Exception as e:
        return await edit_delete(event, f"**عذرًا، حدث خطأ أثناء تحميل الصورة:**\n`{e}`")
    
    await edit_delete(event, "**𓆰 تـم انتحـال الشخـص .. بنجـاح ༗**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحـــال\n⪼ تم انتحـال حسـاب الشخـص ↫ [{first_name}](tg://user?id={user_id}) بنجاح ✅"
        )

@zedub.zed_cmd(pattern="(?:انتحال|نسخ)(?:\s|$)([\s\S]*)")
async def impersonate(event):
    replied_user, error = await get_user_from_event(event)
    if not replied_user:
        return await edit_delete(event, "**يجب الرد على شخص لاستخدام هذا الأمر.**")
    await update_profile(event, replied_user)

@zedub.zed_cmd(pattern=f"{ANTHAL}$")
async def revert(event):
    firstname = DEFAULTUSER
    lastname = gvarstatus("LAST_NAME") or ""
    bio = DEFAULTUSERBIO

    # حذف الصورة
    photos = await event.client.get_profile_photos("me", limit=1)
    if photos:
        await event.client(DeletePhotosRequest(id=[photos[0]]))

    # إعادة المعلومات
    await event.client(functions.account.UpdateProfileRequest(first_name=firstname, last_name=lastname, about=bio))
    await edit_delete(event, "**𓆰 تمت إعـادة الحـسـاب لوضعـه الأصـلـي ✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الغاء_الانتحال\n⪼ تم الغاء الانتحال .. وإعادة الحساب لوضعه الطبيعي ✅"
        )
