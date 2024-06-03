from telebot import types

def create_start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    start_button = types.KeyboardButton(text="Далее")
    keyboard.add(start_button)
    return keyboard

def create_weight_loss_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    weight_loss_button = types.KeyboardButton(text="Похудение")
    keyboard.add(weight_loss_button)
    return keyboard

def create_weight_support_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    weight_support_button = types.KeyboardButton(text="Поддержка формы")
    keyboard.add(weight_support_button)
    return keyboard

def create_muscle_gain_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    muscle_gain_button = types.KeyboardButton(text="Набор мышечной массы")
    keyboard.add(muscle_gain_button)
    return keyboard