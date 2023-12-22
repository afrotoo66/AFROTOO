import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/1105de1e03f0ba27ba095.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@T_Y_E_X"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/T_Y_E_X")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
