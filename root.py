from discord import Client
from asyncio import sleep

client = Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('~test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('~help'):
        await client.send_message(message.channel, '''Type ```~maslina``` to catch maslina.\n
                                                        Type ```~mbag``` to need a madic bag!''')

    elif message.content.startswith('~maslina'):
        voice = await client.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('maslina.mp3')
        player.start()
        await sleep(3)
        await voice.disconnect()
    elif message.content.startswith('~mbag'):
        voice = await client.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('mbag.mp3')
        player.start()
        await sleep(7)
        await voice.disconnect()
    elif message.content.startswith('~loveyou'):
        voice = await client.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('loveyou.mp3')
        player.start()
        await sleep(12)
        await voice.disconnect()

client.run('MzY5MTUzNDcxMzM5MDM2Njcz.DMUa8Q.M0szpAWUzRytxgOyrE7OJfVGvKk')