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
            await event.edit("**Plugin yang anda ketik salah ❌\nMohon ketik plugin dengan benar.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("⚡")
        await asyncio.sleep(3)
        await event.edit("**卍 Stephanie-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 卍**\n\n"
                         f"**◑» Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◑» Pʟᴜɢɪɴ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"╰►| {string} ◄─\n\n")
        await event.reply(f"\n**Contoh** : Ketik » `+help busy` Untuk Informasi Pengunaan Plugin Busy.\nAtau Bisa Juga Dengan Cara, Ketik `+helpme` Untuk Menggunakan Inline Bot Dari @BotFather.\n Jika Tidak Tahu Caranya, Silahkan Bertanya ke » [sini](t.me/Badboyanim) « Terimakasih 🙏")
        await asyncio.sleep(1000)
        await event.delete()
