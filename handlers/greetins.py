from telethon import events
import time
import handlers.client
dyno = handlers.client.client

@events.register(events.NewMessage(outgoing=True,pattern=r"\.hi"))
async def grant(event):
    chat = await event.get_chat()
    await dyno.edit_message(event.message,"Hi , working")



@events.register(events.NewMessage(outgoing=True , pattern=r'\.hello'))
async def greeting(event):
        event.get_chat()
        for i in range(5):
             await dyno.edit_message(event.message , "*h*")
             await dyno.edit_message(event.message , "*h_*")
             await dyno.edit_message(event.message , "*he_*")
             await dyno.edit_message(event.message , "*hel_*")
             await dyno.edit_message(event.message , "*hell_*")
             await dyno.edit_message(event.message , "*hello*")
             await dyno.edit_message(event.message , "*H E L L O*")
             await dyno.edit_message(event.message , 
             "╔┓┏╦━╦┓╔┓╔━━╗\n"
             "║┗┛║┗╣┃║┃║X X  ║\n"
             "║┏┓║┏╣┗╣┗╣╰╯║\n"
             "╚┛┗╩━╩━╩━╩━━╝")
    
@events.register(events.NewMessage(pattern=r'\.helli'))
async def hmlicmd(event):
     chat = event.get_chat()
     for i in range(20):
          await dyno.edit_message(event.message , "▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")
          time.sleep(0.5)
          await dyno.edit_message(event.message , "▬▬.◙.▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻\ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")
          time.sleep(0.5)
          await dyno.edit_message(event.message , "▬.◙.▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")
          time.sleep(0.5)
          await dyno.edit_message(event.message , ".◙. \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻\ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")
          time.sleep(0.5)



@events.register(events.NewMessage( outgoing=True , pattern= r'\.gn'))
async def gnmessage(event):
    for i in range(2):
        chat = await event.get_chat()
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█\n"
        "┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█\n"
        "┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█\n"
        "┌▀█░░█░▌█▐█▐░▌░█░░░▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█\n"
        "┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█\n"
        "┌▀█░░█░▌█▐█▐░▌░█░░░▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█")
        time.sleep(1)
        await dyno.edit_message( event.message , 
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█\n"
        "┌▀█╔══╗╔══╗╔══╗╔══╗▀█\n"
        "┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█\n"
        "┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█\n"
        "┌▀█╚══╝╚══╝╚══╝╚══╝▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█\n"
        "┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█\n"
        "┌▀█░░█░▌█▐█▐░▌░█░░░▀█\n"
        "┌▀█░░░░░░░░░░░░░░░░▀█\n"
        "┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█")
        time.sleep(5)