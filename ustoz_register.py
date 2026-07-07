from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

from config import bot,CHANNEL_ID

from buttons import start_button,phone_button,tasdiq_button

u_router=Router()


class Shogird(StatesGroup):
    shogird=State()
    yosh=State()
    texnologiya=State()
    aloqa=State()
    hudud=State()
    narx=State()
    kasb=State()
    vaqt=State()
    maqsad=State()
    tasdiqlash=State()

@u_router.message(F.text=="Ustoz kerak")
async def ustoz_start_func1(message: Message,state:FSMContext):
    await message.answer("""Ustoz topish uchun ariza berish\n
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
""")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Shogird.shogird)

@u_router.message(Shogird.shogird)
async def ustoz1(message:Message,state:FSMContext):
    await state.update_data(shogird=message.text)
    await message.answer("""🕑 Yosh:\n
Yoshingizni kiriting?\nMasalan, 19
""")
    await state.set_state(Shogird.yosh)

@u_router.message(Shogird.yosh)
async def yosh1(message:Message,state:FSMContext):
    await state.update_data(yosh=message.text)
    await message.answer("""📚 Texnologiya:\n
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan,\n
Java, C++, C#""")
    await state.set_state(Shogird.texnologiya)


@u_router.message(Shogird.texnologiya)
async def texnologiya1(message:Message,state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("""📞 Aloqa:\n
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""",reply_markup=phone_button)
    await state.set_state(Shogird.aloqa)


@u_router.message(Shogird.aloqa)
async def aloqa1(message:Message,state:FSMContext):
    if message.contact :
        phone=message.contact.phone_number
    elif message.text:
        phone=message.text
    await state.update_data(aloqa=phone)
    await message.answer("""🌐 Hudud:\n
Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await state.set_state(Shogird.hudud)


@u_router.message(Shogird.hudud)
async def hudud1(message:Message,state:FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("""💰 Narxi:\n
To'lov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await state.set_state(Shogird.narx)


@u_router.message(Shogird.narx)
async def narx1(message:Message,state:FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("""👨🏻‍💻 Kasbi:\n
Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await state.set_state(Shogird.kasb)

@u_router.message(Shogird.kasb)
async def kasb1(message:Message,state:FSMContext):
    await state.update_data(kasb=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti:\n
Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(Shogird.vaqt)


@u_router.message(Shogird.vaqt)
async def vaqt1(message:Message,state:FSMContext):
    await state.update_data(vaqt=message.text)
    await message.answer("""🔎 Maqsad:\n
Maqsadingizni qisqacha yozib bering.""")
    await state.set_state(Shogird.maqsad)



@u_router.message(Shogird.maqsad)
async def maqsad1(message:Message,state:FSMContext):
    await state.update_data(maqsad=message.text)  
    malumotlar=await state.get_data()
    text=f"""
🎓 Shogird:{malumotlar.get('shogird')}
🕑 Yosh:{malumotlar.get('yosh')}
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
    await state.set_state(Shogird.tasdiqlash)

@u_router.message(Shogird.tasdiqlash)
async def tasdiqlash1(message:Message,state:FSMContext):
    await state.update_data(tasdiqlash=message.text)  
    data = await state.get_data()
    if data['tasdiqlash'] == "HA":
        malumotlar=await state.get_data()
        text=f"""
🎓 Shogird:{malumotlar.get('shogird')}
🕑 Yosh:{malumotlar.get('yosh')}
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