from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
from pyrogram.types.bots_and_keyboards import keyboard_button
import json
import psycopg2

app = Client("MaryamKJ", config_file="config.ini")

user = json.loads(open('secretfiles.json', 'r').read())[
    'postgres']['user']

password = json.loads(open('secretfiles.json', 'r').read())[
    'postgres']['password']

host = json.loads(open('secretfiles.json', 'r').read())[
    'postgres']['host']

port = json.loads(open('secretfiles.json', 'r').read())[
    'postgres']['port']

database = json.loads(open('secretfiles.json', 'r').read())[
    'postgres']['database']


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
async def answer(client, callback_query):

    user_id = callback_query.from_user.id
    
    mark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Gmail", callback_data="Gmail")],
            [InlineKeyboardButton("Instagram", callback_data="Instagram")],
            [InlineKeyboardButton("Others", callback_data="Others")]
        ])      
    await app.send_message(user_id ,"چه اکانتی میخوای ثبت کنی؟ ",reply_markup = mark )


@app.on_callback_query(dynamic_callback_data_filter("old_accounts"))    
async def answer(client, callback_query):
    
    user_id = callback_query.from_user.id

    mark = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Gmail", callback_data="Gmail")],
        [InlineKeyboardButton("Instagram", callback_data="Instagram")],
        [InlineKeyboardButton("Others", callback_data="Others")]
    ])
    await app.send_message(user_id,"چه اکانتی میخوای چک کنی؟ ",reply_markup = mark )
app.run()
