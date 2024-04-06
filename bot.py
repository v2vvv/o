import asyncio
import pyrogram
from pyrogram import Client, filters

app = Client("my_bot")  # Replace "my_bot" with your bot's API ID
app.start()

anti = False

async def bot(shadow, sleeptimet, chat_id, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            await shadow.send_file(chat_id, message.media, caption=message.text)
        else:
            await shadow.send_message(chat_id, message.text)
        await asyncio.sleep(sleeptimet)

@app.on_message(filters.command(".ا", prefixes=".") & filters.outgoing)
async def hussein(client, message):
    await message.delete()

    parameters = message.text.strip().split(maxsplit=2)
    if len(parameters) != 3:
        return await message.reply("اكتب الامر بشكل صحيح")

    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    global anti
    anti = True
    message_to_send = await message.get_reply_message()

    for chat_username in chat_usernames:
        try:
            chat = await app.get_chat(chat_username)
            await bot(app, seconds, chat.id, message_to_send, seconds)
        except Exception as e:
            await message.reply(f"لا يمكن العثور على المجموعة {chat_username}: {str(e)}")
        await asyncio.sleep(1)

app.run()
