#!/usr/bin/env python

import os
import discord
import re
import random
from discord.ext.commands import Bot
from requests_html import HTMLSession



TOKEN = os.getenv("TOKEN")
WORDLIST = {
    'hi-hello': [
        'hi', 
        "hello",
        "hey",
    ]
}
ROADMAP = {
    'frontend': "./assets/roadmaps/frontend.png",
    'backend': "./assets/roadmaps/backend.png",
    'devops': "./assets/roadmaps/devops.png",
    'android': "./assets/roadmaps/android.png",
    'react': "./assets/roadmaps/react.png"
}
KALEEN = {
    "image": './assets/images-1-4.jpeg'
}
BOT_PREFIX = ("?", "!")
INTRO = """
Name: 🔫 **Kaleen Bhaiya!!** (King of Mirzapur)

✅ Hacker News Updator:
COMMAND: `!news`
RESULT: All news from the hacker news page.

COMMAND: !news <news-no>
RESULT: Particular news with link.

✅ Roadmap Provider:
COMMAND: `how`, `start` and a tech needs to be in your message query.
RESULT: PRovide Roadmap.

❌ Don't use word `mirzapur`.

✅ Who is kaleen bhaiya:
COMMAND: kaleen and kon/who needs to be in message.

- @Kaleen
"""


def motivation_pill():
    MOTIVATION_PILL_URL = 'https://api.quotable.io/random'
    response = requests.get(MOTIVATION_PILL_URL)
    res = response.json()
    pill = f"\"{res['content']}\" - {res['author']}"
    return pill


def get_random_qoute():
    with open("ideas.json", "r") as file:
        data = json.load(file)
        return random.choice(data['ideas'])



client = discord.Client()
session = HTMLSession()

@client.event
async def on_message(message):
    """When some one sends the message."""
    username = str(message.author).split("#")[0]
    msg = str(message.content).lower()
    if message.author == client.user:
        return 
    if msg.split(' ')[0] in WORDLIST['hi-hello']:
        msg = msg.split(' ')[0]
    for i in WORDLIST['hi-hello']:
        if i in msg:
            await message.channel.send(f"Suno {username}, ye hi, hello thik hai lekin Mirzapur hamara hai.")
            break
    if 'mirzapur' in msg:
        await message.channel.send(f"Beta {username}, Mirzapur k bare m koi baat nhi karega. Samjhey beta 🔫 hai hamera paas.")
    if 'kaleen' in msg and ('kon' in msg or 'who' in msg):
        with open(KALEEN['image'], 'rb') as image:
            await message.channel.send(file=discord.File(image))
        await message.channel.send(f"{username}, Tumhare baap hai ham!!")

    for tech in ROADMAP.keys():
        if 'how' in msg and 'start' in msg and tech in msg:
            with open(ROADMAP[tech], 'rb') as image:
                await message.channel.send(file=discord.File(image))
            await message.channel.send(f"{username}, Beta isa dekho or padhna chalu karo!!")
            break
    
    if msg.split()[0] == "!news":
        url = "https://news.ycombinator.com/news"
        data = "**Hacker News Updates by Kaleen Bhaiya!**\n\n"
        r = session.get(url)
        a_s = r.html.find("a.storylink", first=False)
        if len(msg.split()) == 1:
            for a in a_s:
                data += str(a_s.index(a) + 1) + ". " + a.text + ".\n"
            await message.channel.send(data)
        elif msg.split()[1].isdigit() and int(msg.split()[1]) < len(a_s) + 1:
            a = a_s[int(msg.split()[1]) - 1]
            data += a.text + ".\n>> " + a.attrs['href']
            await message.channel.send(data)

    if msg == "!help":
        await message.channel.send(INTRO)

    ## For Getting an random quote.
    if msg == "!inspire":
        await message.channel.send(motivation_pill())

    ## For Getting an random idea.
    if msg == "!idea":
        await message.channel.send(get_random_quote())


## Greeting new member when then join the DIVCORN VIRTUAL CAMPS
async def on_member_join(member):

    await member.channel.send(
        f'Hello {member.name}, Welcom in DIVCORN VIRTUAL CAMPUS. \n A Dev community by developers for devlopers' 
    )
    # Create a direct message
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, Welcom in DIVCORN VIRTUAL CAMPUS. \n A Dev community by developers for devlopers' 
    )

    

client.run(TOKEN)
# bot.run(TOKEN)
