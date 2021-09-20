from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
from pyrogram.types.bots_and_keyboards import keyboard_button

app = Client("MaryamKJ", config_file="config.ini")



@app.on_message(filters.command("start"))
async def start_command(Client, message):
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ثبت اکانت جدید", callback_data="hidden_callback_data")],
            [InlineKeyboardButton("اکانت های قدیمی", callback_data="hidden_callback_data")]
        ])
    await app.send_message(message.chat.id , f"سلام {message.from_user.first_name} عزیز لطفا عملیات خود را انتخاب کنید", reply_markup=mark)


@app.on_message(filters.text)
async def plain_text_handler(Client, message):

    text = message.text
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Gmail", callback_data="hidden_callback_data")],
            [InlineKeyboardButton("Instagram", callback_data="hidden_callback_data")],
            [InlineKeyboardButton("Others", callback_data="hidden_callback_data")]
        ])    

    if text == "اکانت های قدیمی" :
        await app.send_message(message.chat.id ,"چه اکانتی میخوای چک کنی؟ ",reply_markup = mark )
    elif text == "ثبت اکانت جدید" :
        await app.send_message(message.chat.id ,"چه اکانتی میخوای ثبت کنی؟ ",reply_markup = mark )

app.run()
