from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

from config import bot,CHANNEL_ID

from buttons import start_button,phone_button,tasdiq_button

sh_router=Router()


class Sherik(StatesGroup):
    sherik=State()
    texnologiya=State()
    aloqa=State()
    telegram=State()
    hudud=State()
    narx=State()
    kasb=State()
    vaqt=State()
    maqsad=State()
    tasdiqlash=State()

@sh_router.message(F.text=="Sherik kerak")
async def sherik_start_func2(message: Message,state:FSMContext):
    await message.answer("""Sherik topish uchun ariza berish\n
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Sherik.sherik)

@sh_router.message(Sherik.sherik)
async def sherik2(message:Message,state:FSMContext):
    await state.update_data(sherik=message.text)
    await message.answer("""📚 Texnologiya:\n
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan,\n
Java, C++, C#""")
    await state.set_state(Sherik.texnologiya)


@sh_router.message(Sherik.texnologiya)
async def texnologiya2(message:Message,state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("""📞 Aloqa:\n
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""",reply_markup=phone_button)
    await state.set_state(Sherik.aloqa)


@sh_router.message(Sherik.aloqa)
async def aloqa2(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    elif message.text:
        phone = message.text
    else:
        await message.answer("Iltimos, telefon raqamingizni pastdagi tugma orqali yuboring yoki matn shaklida yozing!")
        return
    await state.update_data(aloqa=phone)
    await message.answer("""🌐 Hudud:\n
Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await state.set_state(Sherik.hudud)


@sh_router.message(Sherik.hudud)
async def hudud2(message:Message,state:FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("""💰 Narxi:\n
To'lov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await state.set_state(Sherik.narx)


@sh_router.message(Sherik.narx)
async def narx2(message:Message,state:FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("""👨🏻‍💻 Kasbi:\n
Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await state.set_state(Sherik.kasb)

@sh_router.message(Sherik.kasb)
async def kasb2(message:Message,state:FSMContext):
    await state.update_data(kasb=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti:\n
Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(Sherik.vaqt)


@sh_router.message(Sherik.vaqt)
async def vaqt2(message:Message,state:FSMContext):
    await state.update_data(vaqt=message.text)
    await message.answer("""🔎 Maqsad:\n
Maqsadingizni qisqacha yozib bering.""")
    await state.set_state(Sherik.maqsad)



@sh_router.message(Sherik.maqsad)
async def maqsad2(message:Message,state:FSMContext):
    await state.update_data(maqsad=message.text)  
    malumotlar=await state.get_data()
    text=f"""
🏅 Sherik:{malumotlar.get('sherik')}
📚 Texnologiya:{malumotlar.get('texnologiya')}
📞 Aloqa:{malumotlar.get('aloqa')}
🌐 Hudud:{malumotlar.get('hudud')}
💰 Narxi:{malumotlar.get('narx')}
👨🏻‍💻 Kasbi:{malumotlar.get('kasb')}
🕰 Murojaat qilish vaqti:{malumotlar.get('vaqt')}
🔎 Maqsad:{malumotlar.get('maqsad')}
"""
    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=tasdiq_button)
    await state.set_state(Sherik.tasdiqlash)

@sh_router.message(Sherik.tasdiqlash)
async def tasdiqlash2(message:Message,state:FSMContext):
    await state.update_data(tasdiqlash=message.text)  
    data = await state.get_data()
    if data['tasdiqlash'] == "HA":
        malumotlar=await state.get_data()
        text=f"""
🏅 Sherik:{malumotlar.get('sherik')}
📚 Texnologiya:{malumotlar.get('texnologiya')}
📞 Aloqa:{malumotlar.get('aloqa')}
🌐 Hudud:{malumotlar.get('hudud')}
💰 Narxi:{malumotlar.get('narx')}
👨🏻‍💻 Kasbi:{malumotlar.get('kasb')}
🕰 Murojaat qilish vaqti:{malumotlar.get('vaqt')}
🔎 Maqsad:{malumotlar.get('maqsad')}
    """
        await bot.send_message(CHANNEL_ID, text=text)
        await message.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n
E'lon 24-48 soat ichida kanalda chiqariladi.""",reply_markup=start_button)
        await state.clear()
    elif data['tasdiqlash'] == "YO'Q":
        await message.answer("Ma'lumotlar qabul qilinmadi.",reply_markup=start_button)
        await state.clear()
    else:
        await message.answer("Iltimos HA yoki YO'Q deb yozing yoki bitta tugmani bosing:",reply_markup=tasdiq_button)
        return