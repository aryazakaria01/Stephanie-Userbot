# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# Ported by KENZO (Lynx-Userbot)
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For +help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Plugin yang anda ketik salah â\nMohon ketik plugin dengan benar.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("â¡")
        await asyncio.sleep(3)
        await event.edit("**å Stephanie-ððððð½ðð å**\n\n"
                         f"**âÂ» Bá´á´ á´ê° {DEFAULTUSER}**\n**âÂ» PÊá´É¢ÉªÉ´ : {len(modules)}**\n\n"
                         "**â¢ Má´ÉªÉ´ Má´É´á´ :**\n"
                         f"â°âº| {string} ââ\n\n")
        await event.reply(f"\n**Contoh** : Ketik Â» `+help busy` Untuk Informasi Pengunaan Plugin Busy.\nAtau Bisa Juga Dengan Cara, Ketik `+helpme` Untuk Menggunakan Inline Bot Dari @BotFather.\n Jika Tidak Tahu Caranya, Silahkan Bertanya ke Â» [sini](t.me/Badboyanim) Â« Terimakasih ð")
        await asyncio.sleep(1000)
        await event.delete()
