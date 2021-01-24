# Discord RoastBot
import discord
import time
import requests
from bs4 import BeautifulSoup
import random
import asyncio


def letter_split(word):
    return [char for char in word]


def list_to_string(arr):
    str1 = ""
    for i in range(0, len(arr) - 5):
        str1 += arr[i]
    return str1


# Loading in Insult Names
insult_names_source = requests.get('https://www.insult.wiki/list-of-insults')
insult_names_html = insult_names_source.text
insult_names_soup = BeautifulSoup(insult_names_html, features="html.parser")
insult_names_ol = insult_names_soup.find_all('ol')
insult_names_raw = []
for i in insult_names_ol:
    insult_names_raw.append(i.text)
insult_names = insult_names_raw[0].split("\n")

# Loading Thought Catalogue Insults
tc_insults_source = requests.get(
    'https://thoughtcatalog.com/lorenzo-jensen-iii/2016/11/sick-burns-the-100-greatest-insults-of-all-time/')
tc_insults_html = tc_insults_source.text
tc_insults_soup = BeautifulSoup(tc_insults_html, features="html.parser")
tc_insults_ol = tc_insults_soup.find_all('p')
tc_insults = []
for i in tc_insults_ol:
    tc_insults.append(i.text)

# Discord Client Code
client = discord.Client()

variable = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member, message):
    opener_list = [f'Oh for fucks sake! Not {member.name}', f'{member.name} is here and now the fun is over.',
                   f'Great, {member.name} is here! I would have rathered Hitler.',
                   f'{member.name} is here! The human embodiment of a sad handjob.',
                   f'{member.name}, words cannot describe how much ass you eat.',
                   f"{member.name}'s mother is such a milf, 10/10 IGN."]

    await message.channel.send(opener_list[random.randint(0, len(opener_list))])


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    author_arr = letter_split(str(message.author))
    author_name = list_to_string(author_arr)
    user_id = f'<@{message.author.id}>'
    msg = message.content

    if '!hey' in msg:
        await message.channel.send('%s please shut the fuck up' % user_id)
        time.sleep(4)
        await message.channel.send('and stay that way')

    if '!roastme' in msg:
        await message.channel.send(tc_insults[random.randint(3, len(tc_insults) - 3)])

    if '!insultme' in msg:
        await message.channel.send(f'You are a {insult_names[random.randint(1, len(insult_names) - 1)]}')

    if '!rapidfire' in msg:
        counter = 0
        await message.channel.send('Words I would use to describe %s :' % user_id)
        while counter < 5:
            time.sleep(2.5)
            await message.channel.send(insult_names[random.randint(1, len(insult_names) - 1)])
            counter += 1
        time.sleep(3)
        await message.channel.send('Thank you ladies and gentlemen')

    if '!insult' in msg:
        msg_arr = msg.split()
        baz_luck = random.randint(0, 5)
        msg_author = f'<@!{message.author.id}>'
        if msg_arr[1] == '<@!800039039327141919>':
            await message.channel.send('Oh %s, you tried get me to roast myself you %s?' % (
                msg_author, insult_names[random.randint(1, len(insult_names) - 1)]))
            time.sleep(3)
            await message.channel.send(
                '%s , %s' % (msg_author, tc_insults[random.randint(3, len(tc_insults) - 3)]))
        elif msg_arr[1] == '<@!493861916909895702>':
            await message.channel.send('Oh %s, you tried get me to roast my creator you %s?' % (
                msg_author, insult_names[random.randint(1, len(insult_names) - 1)]))
            time.sleep(3)
            await message.channel.send(
                '%s , %s' % (msg_author, tc_insults[random.randint(3, len(tc_insults) - 3)]))
        else:
            await message.channel.send('Hey %s , %s' % (msg_arr[1], tc_insults[random.randint(3, len(tc_insults) - 3)]))
        if baz_luck == 0:
            time.sleep(3)
            await message.channel.send('Bazinga')

    if '!help' in msg:
        await message.channel.send('!hey - Give RoastBot a little poke')
        await message.channel.send('!roastme - RoastBot will flame you like an angry League of Legends virgin')
        await message.channel.send('!insultme - RoastBot will tell you exactly what he thinks of you')
        await message.channel.send('!rapidfire - RoastBot gives you some rapid fire name')
        await message.channel.send('!insult - RoastBot will insult someone for you')

    if '!fart' in msg:
        counter = 0
        while counter < 10:
            await message.channel.send('-play fart reverb')
            counter += 1


client.run('ODAwMDM5MDM5MzI3MTQxOTE5.YAMUag.4MgWNAbEZiM8cFa5sH7aUbNYs3U')
