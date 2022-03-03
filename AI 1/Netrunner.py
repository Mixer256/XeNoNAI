# -*- coding: utf8 -*-
import os, json, requests, random, re
from plugins import gf
from modules import pluginMg
from vkbottle import Bot, Message, keyboard_gen, types
from vkbottle.keyboard import Keyboard, Text

#Основная группа
get_data = gf.loadjson("conf.json")
token = str(get_data['token'])

bot = Bot(token=token)
users_dir = os.path.join(r"users/")

@bot.on.chat_invite()
async def wrapper(ans: Message):
    await ans("‍Большое спасибо за приглашение! Я- Бот XeNoN AI, модель 1! \n\n Выдайте боту доступ переписке или права администратора, в случае если вы не создатель беседы, пользоваться ботом можно через упоминания.")
    
    @bot.on.chat_message()
async def wrapper(ans: Message):
    check_profile = os.path.exists(users_dir + str(ans.from_id) + ".json")
    if check_profile == True:
        pass
    else:
        data = await bot.api.users.get(user_ids=ans.from_id)
        pluginMg.reg(first_name=data[0]['first_name'], last_name=data[0]['last_name'], from_id=ans.from_id)

    text = ans.text
    text = re.sub(r'\[club\w+\|@?.+\]\s', '', text)
    text = re.sub(r'\[club\w+\|@?.+\],\s', '', text)
    text = re.sub('!', '', text)
    text = re.sub('/', '', text)

    MpluginMg = pluginMg.pluginMg(text=text, from_id=ans.from_id)
    if MpluginMg:
        keyboard = Keyboard(one_time=False)
        keyboard.add_row()
        keyboard.add_button(Text(label="📒 Профиль"), color="negative")
        keyboard.add_button(Text(label="💎 Бонус"), color="primary")
        keyboard.add_button(Text(label="🔋 Ферма"), color="primary")
        keyboard.add_row()
        keyboard.add_button(Text(label="📚 Помощь"), color="positive")
        await ans(MpluginMg, keyboard=keyboard.generate())
    else:
        pass
        
        @bot.error_handler(901, 902)
async def error(error):
    print("Cant send message to the user :(, error code:", error[0])

if __name__ == "__main__":
    bot.run_polling()