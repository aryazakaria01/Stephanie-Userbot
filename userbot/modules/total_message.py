from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.totalpesan (.*)")
async def _(event):
    k = await event.get_reply_message()
    if k:
        xx = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"Total PesanDari {u}. Total Obrolan `{xx.total}`")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=u)
    await event.edit(f"Total PesanDari {u}. Total Obrolan `{xx.total}`")

CMD_HELP.update(
    {
        "totalmsg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.totalpesan` | `.tmsg` <username>\
    \n↳ : Mengembalikan jumlah pesan total pengguna dalam obrolan saat ini."
    }
)
