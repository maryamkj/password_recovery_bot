from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
from pyrogram.types.bots_and_keyboards import keyboard_button

app = Client("MaryamKJ", config_file="config.ini")



@app.on_message(filters.command("start"))
async def start_command(Client, message):
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ثبت اکانت جدید", callback_data="new_account")],
            [InlineKeyboardButton("اکانت های قدیمی", callback_data="old_accounts")]
        ])
    await app.send_message(message.chat.id , f"سلام {message.from_user.first_name} عزیز لطفا عملیات خود را انتخاب کنید", reply_markup=mark)

@app.on_message(filters.text)
async def plain_text_handler(Client, message):

    text = message.text
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Gmail", callback_data="Gmail")],
            [InlineKeyboardButton("Instagram", callback_data="Instagram")],
            [InlineKeyboardButton("Others", callback_data="Others")]
        ])    

    if text == "اکانت های قدیمی" :
        await app.send_message(message.chat.id ,"چه اکانتی میخوای چک کنی؟ ",reply_markup = mark )
    elif text == "ثبت اکانت جدید" :
        await app.send_message(message.chat.id ,"چه اکانتی میخوای ثبت کنی؟ ",reply_markup = mark )

@app.on_callback_query()
async def answer(client, callback_query):

    query = callback_query.data
    
    if query == "new_account":
        pass

    elif query == "old_account":
        pass

app.run()
