import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2258849c8eef00541084c.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [à¼ï¸ââ¢äºãðððððãäºâ¢â ](https://t.me/tera_baap_katil)

ðð«ððð­ð¨ð« :- [â¨ à¼ï¸ââ¢äºãðððððãäºâ¢â ](https://t.me/tera_baap_katil)
ðð®ð©ð©ð¨ð«ð­ :- [â¨  âÆ¬Êá´ï¸»â¦â¤âð»ð¾ï¸ðð´ðð ð¿ï¸ð¾ï¸ð¸ð½ðââ¤â¦ï¸»ã](https://t.me/FULL_MASTI_CLUBS)
ðð¢ð¬ðð®ð¬ð¬ :- [â¨  HEART BROKEN ð PERSON](https://t.me/heartbrokenperson1)
ðð¨ð®ð«ðð  :- [â¨  ðð¹ð¶ð°ð¸ âï¸ ð¥ð²ð½ð¼ ð](https://t.me/FULL_MASTI_CLUBS)



ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [à¼ï¸ââ¢äºãðððððãäºâ¢â ](https://t.me/tera_baap_katil)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/heartbrokenperson1")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2258849c8eef00541084c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://t.me/heartbrokenperson1")
                ]
            ]
        ),
    )
