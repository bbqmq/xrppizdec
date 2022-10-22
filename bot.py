from aiogram.types import Message

from utils.main.chats import Chat


async def bot_added_to_chat(message: Message):
    Chat(chat=message.chat)
    return await message.answer('⚉ <b>СПАСИБО ЧТО ДОБАВИЛ МЕНЯ В ЧАТ</b> ⚇\n'
                                '❤ Введи: "Помощь" (меню помощи)\n' 
                                '🅰️ Админ: <a href="https://t.me/vaster_o">ОСНОВАТЕЛЬ</a>\n' 
                                '🕹 Игровой чат: @nanik_chat\n'
                                '📺 Главные новости бота: @nanik_channel'
                                )
