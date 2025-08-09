import asyncio
import os
from io import BytesIO
from random import randint
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont
from requests import get

from zedthon import zed_cmd
from zedthon.Config import Config
from zedthon.core.managers import edit_or_reply

plugin_category = "extra"


async def amongus_gen(text: str, clr: int) -> str:
    url = "https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/Amongus/"
    font = ImageFont.truetype(
        BytesIO(
            get(
                "https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/fonts/bold.ttf"
            ).content
        ),
        60,
    )
    imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    text_ = "\n".join("\n".join(wrap(part, 30)) for part in text.split("\n"))
    w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text_img = Image.new("RGBA", (w + 30, h + 30))
    ImageDraw.Draw(text_img).multiline_text(
        (15, 15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000"
    )
    w_total = imposter.width + text_img.width + 10
    h_total = max(imposter.height, text_img.height)
    image = Image.new("RGBA", (w_total, h_total))
    image.paste(imposter, (0, h_total - imposter.height), imposter)
    image.paste(text_img, (w_total - text_img.width, 0), text_img)
    image.thumbnail((512, 512))
    webp_file = os.path.join(Config.TEMP_DIR, "imposter.webp")
    image.save(webp_file, "WebP")
    return webp_file

#ريفز
async def get_imposter_img(text: str) -> str:
    background = get(
        f"https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/imposter/impostor{randint(1,22)}.png"
    ).content
    font_data = get(
        "https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/fonts/roboto_regular.ttf"
    ).content
    font = ImageFont.truetype(BytesIO(font_data), 30)
    image = Image.open(BytesIO(background))
    x, y = image.size
    draw = ImageDraw.Draw(image)
    w, h = draw.multiline_textsize(text=text, font=font)
    draw.multiline_text(
        ((x - w) // 2, (y - h) // 2), text=text, font=font, fill="white", align="center"
    )
    webp_file = os.path.join(Config.TEMP_DIR, "impostor.png")
    image.save(webp_file, "png")
    return webp_file


@zed_cmd(
    pattern="من القاتل(|بريء) ([\s\S]*)",
    command=("من القاتل", plugin_category),
)
async def _(event):
    """أنميشن من القاتل مع ملصقات"""
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()

    text1 = await edit_or_reply(event, "᯽︙ هممم اكيـد اكو شـخص مات !!")
    await asyncio.sleep(2)
    await text1.delete()

    stcr1 = await event.client.send_file(event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg")
    text2 = await event.reply(f"**لقد عـملت اجـتماع هـام**")
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()

    stcr2 = await event.client.send_file(event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg")
    text3 = await event.reply(f"**نحـن 3 يجـب ان نصوت علـى احـد او نخـسر**")
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()

    stcr3 = await event.client.send_file(event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg")
    text4 = await event.reply(f"**- الاخـرين :** أيــن??? ")
    await asyncio.sleep(2)
    await text4.edit(f"**- الاخـرين :** مــن ?? ")
    await asyncio.sleep(2)
    await text4.edit(f"**أنـه {name} , لقـد شاهـدت {name}  يستـخدم الفيـنت**")
    await asyncio.sleep(3)
    await text4.edit(f"**- الاخـرين :** حسـنا .. صـوتوا علـى {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()

    stcr4 = await event.client.send_file(event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg")
    catevent = await event.reply(f"**᯽︙  {name} تـم استـبعاده .......**")
    await asyncio.sleep(2)

    for frame in [
        "ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ",
        "ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ",
        "ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ",
        "ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ",
        "ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ",
        "ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ",
        "ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ",
        "ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ",
        "ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ",
        "ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ",
    ]:
        await catevent.edit(frame)
        await asyncio.sleep(0.5)

    await stcr4.delete()
    if cmd == "":
        await catevent.edit(f"ඞ  {name} لقـد كـان الـقاتل.")
    else:
        await catevent.edit(f"ඞ  {name} لـم يـكن الـقاتل.")
    await asyncio.sleep(4)
    await catevent.delete()


@zed_cmd(
    pattern="القاتل(|بريء) ([\s\S]*)",
    command=("القاتل", plugin_category),
)
async def _(event):
    """أنميشن من القاتل نص فقط"""
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()

    catevent = await edit_or_reply(event, f"{name} تـم اخـراجـه.......")
    await asyncio.sleep(2)

    for frame in [
        "ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ",
        "ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ",
        "ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ",
        "ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ",
        "ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ",
        "ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ",
        "ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ",
        "ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ",
        "ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ",
        "ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ",
    ]:
        await catevent.edit(frame)
        await asyncio.sleep(0.8)

    if cmd == "":
        await catevent.edit(f"ඞ  {name} لقـد كـان الـقاتل.")
    else:
        await catevent.edit(f"ඞ  {name} لـم يـكن الـقاتل.")
