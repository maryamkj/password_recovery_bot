from pyrogram import Client
from pyrogram import filters

app = Client("MaryamKJ", config_file="config.ini")



@app.on_message(filters.command("start"))
async def start_command(Client, message):
    await app.send_message(message.chat.id , "Hello, let's get started" )


app.run()
