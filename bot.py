# async import
import asyncio
# config import
from config import bot,dp
# aiogram import
from aiogram.types import Message
from aiogram.filters import Command
# buttons import
from buttons import start_button

from sherik_register import sh_router
from shogird_register import o_router
from hodim_register import h_router
from ustoz_register import u_router
from ish_joy_register import i_router

@dp.message(Command('start'))
async def start_function(message:Message):
    await message.answer(f"""Assalom alaykum {message.from_user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!\n
/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""",reply_markup=start_button)

@dp.message(Command('help'))
async def help_function(message:Message):
    await message.answer("""UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. \n
Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. \n
E'lon berish: @UstozShogird98Bot\n
Admin @UstozShogirdAdminBot""")

dp.include_router(i_router)
dp.include_router(sh_router)
dp.include_router(h_router)
dp.include_router(o_router)
dp.include_router(u_router)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    print("Bot ishlayapti.")
    asyncio.run(main())