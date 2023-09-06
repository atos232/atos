from telethon import events
import handlers.client
dyno = handlers.client.client




@events.register(events.NewMessage(outgoing=True , pattern=r'\.alive'))
async def alivecmd(event):
    chat = await event.get_chat()
    await dyno.delete_messages(chat , event.message)
    photo = 'https://graph.org/file/e25ef380020a3f3268624.mp4'
    me= await dyno.get_me()
    await dyno.send_file(chat , file=photo , caption=
                         "THE USERBOT\n\n"
                         "Userbot is alive currently\n"
                         "userbot Copied by NoobKid"
                         "python : Python 3.11.2\n"
                         "Telethon : Telethon 1.28.5\n"
                         "BOT VERSION : 0.00.1\n"
                         "REPO : [SECRET](https://github.com/SHADOW-UB/Shadow-Userbot)".format(me.username)
                         )








@events.register(events.NewMessage( incoming=True , pattern='@D_yno'))
async def ontag(event):
    chat = await event.get_chat()
    await event.reply("SORRY NIGGA , YOU'RE NOT WORTHY OF TALKING TO MY MASTER")
