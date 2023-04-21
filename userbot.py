from telethon import TelegramClient , events , Button
import time , logging , os , asyncio 
import handlers.client , handlers.greetins , handlers.alive , handlers.quote , handlers.telegraph , handlers.pin
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = handlers.client.api_id
api_hash = handlers.client.api_hash
bot_teku = handlers.client.bot_token
usrid = handlers.client.id
BOTUSRNAME = handlers.client.bot_username

botClient = TelegramClient('bot' , api_id , api_hash).start(bot_token=bot_teku)
dyno = handlers.client.client

with dyno as shadow:
    shadow.add_event_handler(handlers.pin.pincmd)

with dyno as shadow:
    shadow.add_event_handler(handlers.pin.unpincmd)

with dyno as shadow:
    shadow.add_event_handler(handlers.telegraph.telegraphcmd)

with dyno as shadow:
    shadow.add_event_handler(handlers.greetins.grant)

with dyno as shadow:
    shadow.add_event_handler(handlers.greetins.greeting)

with dyno as shadow:
    shadow.add_event_handler(handlers.greetins.gnmessage)

with dyno as shadow:
    shadow.add_event_handler(handlers.alive.alivecmd)    

with dyno as shadow:
    shadow.add_event_handler(handlers.alive.ontag)

with dyno as shadow:
    shadow.add_event_handler(handlers.quote.qutecmd)

with dyno as shadow:
    shadow.add_event_handler(handlers.greetins.hmlicmd)

@botClient.on(events.InlineQuery)
async def iquery(query):
    result = query.builder.article('Help' , text= "Help Menu" , buttons=[
        [Button.inline("PLUGINS" , data=b'plug')]
    ])
    await query.answer([result])

@dyno.on(events.NewMessage(outgoing=True , pattern=r'\.help'))
async def helphand(event):
    results = await dyno.inline_query(BOTUSRNAME, 'help')
    await results[0].click(event.chat_id)
    chat = await event.get_chat()
    await dyno.delete_messages(chat , event.message)

@botClient.on(events.CallbackQuery)
async def callbackcmd(event):
    if event.original_update.user_id == usrid :
         if event.data == b'plug':
             await event.answer("PLUGINS : \n"
                           ".hello\n"
                           ".alive\n"
                           ".tm\n"
                           ".update\n"
                           ".q" , alert=True )
    else:
         await event.answer("YOu'RE NOT THE BOT OWNER\n"
                            "GO AWAY NIGGA", alert=True)

@events.register(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    await botClient.send_message(SENDER ,  "THIS IS THE BOT OF MY MASTER USERBOT\n"
                                 "       How can i help u...")

loop = asyncio.get_event_loop()
dyno.start()
botClient.start()
print("bot running")
loop.run_forever()