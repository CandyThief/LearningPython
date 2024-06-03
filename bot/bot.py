# Импорт необходимых модулей
import telebot
from telebot import types
from bot_init import bot  # Импорт объекта бота
from keyboard_utils import *

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Приветственное сообщение
    bot.send_message(message.chat.id, "Привет! Я фитнес-бот! Чтобы начать, нажми кнопку 'Далее'.", reply_markup=create_next_keyboard())

# Обработчик кнопки "Далее"
@bot.message_handler(func=lambda message: message.text == "Далее")
def handle_next_button(message):
    # Предоставление выбора цели среди трех вариантов
    bot.send_message(message.chat.id, "Выбери свою цель:", reply_markup=create_goal_choice_keyboard())

# Обработчики выбора цели
@bot.message_handler(func=lambda message: message.text in ["Похудение", "Поддержка формы", "Набор мышечной массы"])
def handle_goal_choice(message):
    goal = message.text
    bot.send_message(message.chat.id, f"Твоя цель: {goal}. Теперь мы можем начать работу над ней.")

# Функции для создания клавиатур
def create_next_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    next_button = types.KeyboardButton(text="Далее")
    keyboard.add(next_button)
    return keyboard

def create_goal_choice_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    weight_loss_button = types.KeyboardButton(text="Похудение")
    weight_support_button = types.KeyboardButton(text="Поддержка формы")
    muscle_gain_button = types.KeyboardButton(text="Набор мышечной массы")
    keyboard.add(weight_loss_button, weight_support_button, muscle_gain_button)
    return keyboard

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
