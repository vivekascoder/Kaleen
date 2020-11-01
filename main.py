#!/usr/bin/env python

import discord
import re

TOKEN = "----"

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

client = discord.Client()

@client.event
async def on_message(message):
    """When some one sends the message."""
    username = str(message.author).split("#")[0]
    msg = str(message.content).lower()
    if message.author == client.user:
        return 
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


client.run(TOKEN)