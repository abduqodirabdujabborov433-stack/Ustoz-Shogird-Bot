from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

start_button=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"),KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak"),KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Shogird kerak")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone_button=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqam ulashish.",request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
tasdiq_button=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="HA"),KeyboardButton(text="YO'Q")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)