from replit import db
import os
import discord
import get_memes
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # print(message.channel.name)
    # print(dir(message.channel))
    # print(message.author)
    if (str(message.author) == os.environ['author']):
        if (message.content == "clr msg all"):
            async for msg in message.channel.history(limit=200):
                await msg.delete()
            donemsg = await message.channel.send('done')
            await donemsg.delete(delay=5)
        elif (message.content == "clr msg"):
            async for msg in message.channel.history(limit=4):
                await msg.delete()
            donemsg = await message.channel.send('done')
            await donemsg.delete(delay=5)
            # messages = await message.channel.history(limit=123).flatten()
            # for m in messages:
            #   await m.delete()

    if message.content.startswith('memes') or message.content.startswith(
            'Memes') or message.content.startswith(
                'MEMES') or message.content.startswith(
                    'meme') or message.content.startswith('Meme'):
        meme = get_memes.GETmemes()
        await message.channel.send(meme[1])
        await message.channel.send(meme[0])


async def send_msg(msg, txt):
    if txt:
        await msg.channel.send(txt)


async def send_msg_and_del(msg, txt):
    mymsg = await msg.channel.send(txt)
    await mymsg.delete(delay=5)


def add_to_db(key, val):
    if key in get_db_keys():
        db[key].append(val)
    else:
        db[key] = []
        db[key].append(val)


def get_db_keys():
    return db.keys()


keep_alive()
token = os.environ['TOKEN']
client.run(token)
