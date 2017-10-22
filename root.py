'''
Discord bot S.T.A.L.K.E.R.
Plays best sounds we found on the Internet
'''
from asyncio import sleep
from discord import Client

CLIENT = Client()

@CLIENT.event
async def on_ready():
    '''
    Function for CLIENT.run() that executes when bot is ready
    '''
    print('Logged in as')
    print(CLIENT.user.name)
    print(CLIENT.user.id)
    print('------')

@CLIENT.event
async def on_message(message):
    '''
    Main function that does all magic
    '''
    if message.content.startswith('~test'):
        counter = 0
        tmp = await CLIENT.send_message(message.channel, 'Calculating messages...')
        async for log in CLIENT.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await CLIENT.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('~help'):
        await CLIENT.send_message(message.channel, '''Type ```~maslina``` to catch maslina.\n
                                                        Type ```~mbag``` to need a madic bag!''')

    elif message.content.startswith('~maslina'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('maslina.mp3')
        player.start()
        await sleep(3)
        await voice.disconnect()
    elif message.content.startswith('~mbag'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('mbag.mp3')
        player.start()
        await sleep(7)
        await voice.disconnect()
    elif message.content.startswith('~loveyou'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('loveyou.mp3')
        player.start()
        await sleep(12)
        await voice.disconnect()
    elif message.content.startswith('~stop'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('stop.mp3')
        player.start()
        await sleep(7)
        await voice.disconnect()
    elif message.content.startswith('~nope'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('nope.mp3')
        player.start()
        await sleep(2)
        await voice.disconnect()
    elif message.content.startswith('~illuminati'):
        voice = await CLIENT.join_voice_channel(message.author.voice.voice_channel)
        player = voice.create_ffmpeg_player('illuminati.mp3')
        player.start()
        await sleep(12)
        await voice.disconnect()

CLIENT.run('MzY5MTUzNDcxMzM5MDM2Njcz.DMewjA.U8B5JDkDCJg3KEi3Ik9IQbXR1rU')
