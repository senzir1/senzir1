import html
import os
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import PhotoCropSizeSmallError, ImageProcessFailedError, StickerMimeInvalidError

from ..Config import Config
from . import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, zedub, edit_delete, get_user_from_event
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = Config.DEFAULT_BIO or "- ‏وحدي أضيء، وحدي أنطفئ انا قمري و كُل نجومي..🤍"
ANTHAL = gvarstatus("ANTHAL") or "(إعـادة الحـسـاب|اعادة|اعاده)"

@zedub.zed_cmd(pattern="نسخ|انتحال(?:\s|$)([\s\S]*)")
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return await edit_delete(event, "**لم يتم العثور على المستخدم!**")

    user_id = replied_user.id

    # تحميل صورة الملف الشخصي
    profile_pic = None
    try:
        profile_pic = await event.client.download_profile_photo(user_id, file=Config.TEMP_DIR)
    except Exception:
        profile_pic = None

    # جلب الاسم والنبذة
    first_name = html.escape(replied_user.first_name or "").replace("\u2060", "")
    last_name = html.escape(replied_user.last_name or "").replace("\u2060", "") if replied_user.last_name else "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    full_user = await event.client(GetFullUserRequest(user_id))
    user_bio = full_user.full_user.about or " "

    # تحديث البيانات الشخصية
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))

    # رفع الصورة الشخصية
    if profile_pic:
        try:
            pfile = await event.client.upload_file(profile_pic)
            await event.client(functions.photos.UploadProfilePhotoRequest(file=pfile))
        except (PhotoCropSizeSmallError, ImageProcessFailedError, StickerMimeInvalidError):
            await edit_delete(event, "**⚠️ لم يتم رفع الصورة: قد تكون غير مدعومة أو صغيرة جدًا.**")
            return
        except Exception as e:
            await edit_delete(event, f"**⚠️ خطأ أثناء رفع الصورة:**\n`{e}`")
            return

    await edit_delete(event, "**✅ تم الانتحال بنجاح!**")

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحـــال\n ⪼ تم انتحـال حسـاب الشخـص ↫ [{first_name}](tg://user?id={user_id}) بنجاح ✅"
        )
