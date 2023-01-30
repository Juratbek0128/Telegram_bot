"""

Bu qidiruv boti

"""
import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6029761996:AAEpbDI8YQBHrFoIJt4Eew3UzNT5niaCvMY'
wikipedia.set_lang('uz')
# Jurnal yozishni sozlang
logging.basicConfig(level=logging.INFO)
# Bot va dispetcherni ishga tushiring
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Ushbu ishlov beruvchi foydalanuvchi `/start` yoki `/help` buyrug'ini yuborganda chaqiriladi
    """
    await message.reply("Salom!  Men Search_bot!\nMenga qidirmoqchi bo'lgan narsangizni nomini kiriting.\nO'zbekiston tilida kiriting.")
@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond=wikipedia.summary(message.text)
        await message.answer(respond)    # agar topilsa bu 
    except:
        await message.answer("Bu mavzuga oid maqola ya'ni malumot topilmadi") # agar har qanday holatda ham xatolik yuz bersa xato
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



