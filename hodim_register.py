from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

from config import bot,CHANNEL_ID

from buttons import start_button,tasdiq_button,phone_button

h_router=Router()


class Xodim(StatesGroup):
    idora=State()
    texnologiya=State()
    aloqa=State()
    hudud=State()
    masul=State()
    vaqt=State()
    ish_vaqt=State()
    maosh=State()
    qoshimcha=State()
    tasdiqlash=State()

@h_router.message(F.text=="Xodim kerak")
async def Xodim_start_func3(message: Message,state:FSMContext):
    await message.answer("""Xodim topish uchun ariza berish\n
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("🎓 Idora nomi?")
    await state.set_state(Xodim.idora)

@h_router.message(Xodim.idora)
async def idora3(message:Message,state:FSMContext):
    await state.update_data(idora=message.text)
    await message.answer("""📚 Texnologiya:\n
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan,\n
Java, C++, C#""")
    await state.set_state(Xodim.texnologiya)


@h_router.message(Xodim.texnologiya)
async def texnologiya3(message:Message,state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("""📞 Aloqa:\n
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""",reply_markup=phone_button)
    await state.set_state(Xodim.aloqa)


@h_router.message(Xodim.aloqa)
async def aloqa3(message: Message, state: FSMContext):
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
    await state.set_state(Xodim.hudud)

@h_router.message(Xodim.hudud)
async def hudud3(message:Message,state:FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("""✍️Mas'ul ism sharifi?""")
    await state.set_state(Xodim.masul)

@h_router.message(Xodim.masul)
async def masul3(message:Message,state:FSMContext):
    await state.update_data(masul=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti: \n
Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(Xodim.vaqt)


@h_router.message(Xodim.vaqt)
async def vaqt3(message:Message,state:FSMContext):
    await state.update_data(vaqt=message.text)
    await message.answer("""🕰 Ish vaqtini kiriting?""")
    await state.set_state(Xodim.ish_vaqt)

@h_router.message(Xodim.ish_vaqt)
async def ish_vaqt3(message:Message,state:FSMContext):
    await state.update_data(ish_vaqt=message.text)
    await message.answer("""💰 Maoshni kiriting?""")
    await state.set_state(Xodim.maosh)

@h_router.message(Xodim.maosh)
async def maosh3(message:Message,state:FSMContext):
    await state.update_data(maosh=message.text)
    await message.answer("""‼️ Qo`shimcha ma`lumotlar?""")
    await state.set_state(Xodim.qoshimcha)


@h_router.message(Xodim.qoshimcha)
async def qoshimcha3(message:Message,state:FSMContext):
    await state.update_data(qoshimcha=message.text)  
    malumotlar=await state.get_data()
    text=f"""
🏢 Idora:{malumotlar.get('idora')}
📚 Texnologiya:{malumotlar.get('texnologiya')}
📞 Aloqa:{malumotlar.get('aloqa')}
🌐 Hudud:{malumotlar.get('hudud')}
✍️ Mas'ul:{malumotlar.get('masul')}
🕰 Murojaat vaqti:{malumotlar.get('vaqt')}
🕰 Ish vaqti:{malumotlar.get('ish_vaqt')}
💰 Maosh:{malumotlar.get('maosh')}
‼️ Qo'shimcha:{malumotlar.get('qoshimcha')}
"""
    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=tasdiq_button)
    await state.set_state(Xodim.tasdiqlash)

@h_router.message(Xodim.tasdiqlash)
async def tasdiqlash3(message:Message,state:FSMContext):
    await state.update_data(tasdiqlash=message.text)  
    data = await state.get_data()
    if data['tasdiqlash'] == "HA":
        malumotlar=await state.get_data()
        text=f"""
🏢 Idora:{malumotlar.get('idora')}
📚 Texnologiya:{malumotlar.get('texnologiya')}
📞 Aloqa:{malumotlar.get('aloqa')}
🌐 Hudud:{malumotlar.get('hudud')}
✍️ Mas'ul:{malumotlar.get('masul')}
🕰 Murojaat vaqti:{malumotlar.get('vaqt')}
🕰 Ish vaqti:{malumotlar.get('ish_vaqt')}
💰 Maosh:{malumotlar.get('maosh')}
‼️ Qo'shimcha:{malumotlar.get('qoshimcha')}
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