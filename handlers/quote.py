from telethon import events , TelegramClient
import handlers.client
dyno= handlers.client.client


@dyno.on(events.NewMessage(pattern=r'\.q'))
async def qutecmd(event):
    chat = await event.get_chat()
    replied_msg = await event.get_reply_message()
    await dyno.edit_message(event.message , "working in it......")
    x = await replied_msg.forward_to('@QuotLyBot')
    async with dyno.conversation('@QuotLyBot') as conv:
        xx = await conv.get_response(x.id)
        await dyno.send_read_acknowledge(conv.chat_id)
        await dyno.send_message(chat , xx)
        await event.message.delete()