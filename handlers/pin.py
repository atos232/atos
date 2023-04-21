from telethon import events
import handlers.client

dyno = handlers.client.client

@dyno.on(events.NewMessage(outgoing=True,pattern=r'\.pin'))
async def pincmd(event):
    chat = await event.get_chat()
    if event.is_reply:
        r = await event.get_reply_message()
        await r.pin()
        await dyno.edit_message(event.message , "`pinned the tagged message`")
    else:
        await dyno.edit_message(event.message,"`reply to a message`")

@dyno.on(events.NewMessage(outgoing=True,pattern=r'\.unpin'))
async def unpincmd(event):
    chat = await event.get_chat()
    if event.is_reply:
        r = await event.get_reply_message()
        await r.unpin()
        await dyno.edit_message(event.message , "`unpinned the tagged message`")
    else:
        await dyno.edit_message(event.message,"`reply to a message`")