# Created by Apis
# Jan hapus credit ya anjing!!!

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.developer(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        f"__Berikut Developer Repo Userbot Kami :__ "
        f"• [Arya Zakaria](https://t.me/Badboyanim) "
        f"• [Apis](https://t.me/PacarFerdilla) \n\n"
        f" - - - - - - - - - - - - - - - - - -  \n"
        f" - - S T E P H A N I E U S E R B O T - - \n"
        f" - - - - - - - - - - - - - - - - - - ")

CMD_HELP.update(
    {
        "developer": "__**Modules**__ `developer`\
        \n\n  •  __**Command**__ :** `.developer`\
        \n  •  __Penjelasan : __Untuk Mengecek Daftar Developer Pada Userbot\
    "
    }
)
