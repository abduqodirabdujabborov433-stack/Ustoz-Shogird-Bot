from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

from config import bot,CHANNEL_ID

from buttons import start_button,phone_button,tasdiq_button

o_router=Router()


class Shogird(StatesGroup):
    ustoz=State()
    yosh=State()
    texnologiya=State()
    aloqa=State()
    hudud=State()
    narx=State()
    kasb=State()
    vaqt=State()
    maqsad=State()
    tasdiqlash=State()

@o_router.message(F.text=="Shogird kerak")
async def shogird_start_func5(message: Message,state:FSMContext):
    await message.answer("""Shogird topish uchun ariza berish\n
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
""")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Shogird.ustoz)

@o_router.message(Shogird.ustoz)
async def shogird5(message:Message,state:FSMContext):
    await state.update_data(ustoz=message.text)
    await message.answer("""🕑 Yosh:\n
Yoshingizni kiriting?\nMasalan, 19
""")
    await state.set_state(Shogird.yosh)

@o_router.message(Shogird.yosh)
async def yosh5(message:Message,state:FSMContext):
    await state.update_data(yosh=message.text)
    await message.answer("""📚 Texnologiya:\n
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan,\n
Java, C++, C#""")
    await state.set_state(Shogird.texnologiya)


@o_router.message(Shogird.texnologiya)
async def texnologiya5(message:Message,state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("""📞 Aloqa:\n
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""",reply_markup=phone_button)
    await state.set_state(Shogird.aloqa)


@o_router.message(Shogird.aloqa)
async def aloqa5(message:Message,state:FSMContext):
    if message.contact :
        phone=message.contact.phone_number
    elif message.text:
        phone=message.text
    await state.update_data(aloqa=phone)
    await message.answer("""🌐 Hudud:\n
Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await state.set_state(Shogird.hudud)


@o_router.message(Shogird.hudud)
async def hudud5(message:Message,state:FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("""💰 Narxi:\n
To'lov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await state.set_state(Shogird.narx)


@o_router.message(Shogird.narx)
async def narx5(message:Message,state:FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("""👨🏻‍💻 Kasbi:\n
Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await state.set_state(Shogird.kasb)

@o_router.message(Shogird.kasb)
async def kasb5(message:Message,state:FSMContext):
    await state.update_data(kasb=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti:\n
Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(Shogird.vaqt)


@o_router.message(Shogird.vaqt)
async def vaqt5(message:Message,state:FSMContext):
    await state.update_data(vaqt=message.text)
    await message.answer("""🔎 Maqsad:\n
Maqsadingizni qisqacha yozib bering.""")
    await state.set_state(Shogird.maqsad)



@o_router.message(Shogird.maqsad)
async def maqsad5(message:Message,state:FSMContext):
    await state.update_data(maqsad=message.text)  
    malumotlar=await state.get_data()
    text=f"""
🎓 Ustoz:{malumotlar.get('ustoz')}
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

@o_router.message(Shogird.tasdiqlash)
async def tasdiqlash5(message:Message,state:FSMContext):
    await state.update_data(tasdiqlash=message.text)  
    data = await state.get_data()
    if data['tasdiqlash'] == "HA":
        malumotlar=await state.get_data()
        text=f"""
🎓 Ustoz:{malumotlar.get('ustoz')}
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