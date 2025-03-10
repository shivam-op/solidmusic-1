from pyrogram import filters, Client
from pyrogram.types import Message

from core.clients import user
from database.lang_utils import get_message as gm


@Client.on_message(filters.command("gcast"))
async def gcast_(_, message: Message):
    text = " ".join(message.command[1:])
    msg = await message.reply(gm(message.chat.id, "process_gcast"))
    error = success = 0
    async for dialog in user.iter_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            chat_id = dialog.chat.id
            try:
                success += 1
                await user.send_message(chat_id, text)
            except Exception as e:
                print(e)
                error += 1
    return await msg.edit(gm(message.chat.id, "success_gcast").format(str(success), str(error)))
