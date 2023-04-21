from telethon import events
import time , os , handlers.client
from html_telegraph_poster.upload_images import upload_image
dyno = handlers.client.client

@dyno.on(events.NewMessage(outgoing=True,pattern=r"\.tm"))
async def telegraphcmd(event):
    chat = await event.get_chat()
    replied = await event.get_reply_message()
    await dyno.edit_message(event.message , "working in it........")
    try:
        image = await replied.download_media()
        g = upload_image(image)
    except:
        return await dyno.edit_message(event.message , "Reply to a Image")
    
    time.sleep(5)
    await dyno.edit_message(event.message , g , link_preview=False)
    os.remove(image)
    