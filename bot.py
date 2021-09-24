from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
from pyrogram.types.bots_and_keyboards import keyboard_button
import constants as keys
import psycopg2

app = Client("MaryamKJ", config_file="config.ini")


def dynamic_callback_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data

    return filters.create(func, data=data)

@app.on_message(filters.command("start"))
async def start_command(Client, message):
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ثبت اکانت جدید", callback_data="new_account")],
            [InlineKeyboardButton("اکانت های قدیمی", callback_data="old_accounts")]
        ])
    await app.send_message(message.chat.id , f"سلام {message.from_user.first_name} عزیز لطفا عملیات خود را انتخاب کنید", reply_markup=mark)


@app.on_callback_query(dynamic_callback_data_filter("new_account"))    
async def new_account_answer(client, callback_query):

    user_id = callback_query.from_user.id
    
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Gmail", callback_data="new_gmail")],
            [InlineKeyboardButton("Instagram", callback_data="new_instagram")],
            [InlineKeyboardButton("Others", callback_data="new_others")]
        ])      
    await app.send_message(user_id ,"چه اکانتی میخوای ثبت کنی؟ ",reply_markup = mark )


@app.on_callback_query(dynamic_callback_data_filter("old_accounts"))    
async def old_accounts_answer(client, callback_query):
    
    user_id = callback_query.from_user.id

    mark = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Gmail", callback_data="old_gmail")],
        [InlineKeyboardButton("Instagram", callback_data="old_instagram")],
        [InlineKeyboardButton("Others", callback_data="old_others")]
    ])
    await app.send_message(user_id,"چه اکانتی میخوای چک کنی؟ ",reply_markup = mark )


@app.on_callback_query(dynamic_callback_data_filter("new_gmail"))    
async def create_new_gmail(client, callback_query):

    user_id = callback_query.from_user.id
    await app.send_message(user_id ,"یوزرنیم خودتون رو وارد کنید",reply_markup = ForceReply(True) )



app.run()

