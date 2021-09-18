from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *

app = Client("MaryamKJ", config_file="config.ini")



@app.on_message(filters.command("start"))
async def start_command(Client, message):
    mark = ReplyKeyboardMarkup([
        [" ثبت اکانت جدید "," اکانت های قدیمی "]
    ],resize_keyboard=True, one_time_keyboard=True)
    
    await app.send_message(message.chat.id , f"سلام {message.from_user.first_name} عزیز لطفا عملیات خود را انتخاب کنید", reply_markup=mark)


app.run()
