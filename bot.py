from pyrogram import Client

app = Client("MaryamKJ", config_file="config.ini")



@app.on_message()
async def test(Client, message):
    await app.send_message(message.chat.id , "Hello, let's get started" )


app.run()
