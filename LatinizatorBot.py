import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Установка переменной окружения для токена бота
# Инициализация бота и диспетчера
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Логирование в файл
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

# Транслитерация в соответствии с приказом
transliteration_rules = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
    'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E',
    'Ю': 'Yu', 'Я': 'Ya', 'Ъ': '', 'Ь': '',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e',
    'ю': 'yu', 'я': 'ya', 'ъ': '', 'ь': ''
}

def transliterate(text):
    result = ""
    for char in text:
        result += transliteration_rules.get(char, char)
    return result

# Хэндлер для команды /start
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

# Хэндлер для всех текстовых сообщений
@dp.message()
async def transliterate_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    original_text = message.text
    transliterated_text = transliterate(original_text)
    logging.info(f'{user_name} {user_id}: {original_text} -> {transliterated_text}')
    await message.answer(text=transliterated_text)

# Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)