import discord
import random
import pyttsx3
import uberduck

ducky = uberduck.UberDuck('pub_dselihpqtypbbwkxhj', 'pk_7a26317f-d500-4abd-87d8-83fb6721cc8c')
voices = uberduck.get_voices(return_only_names = True)
voices_message = ''
TOKEN = 'OTI4NjI4ODY1MTM0MzkxMzQ2.GZSFQN.B4pbbxIRYJB68u0dDfN_INvRDfYD3U6-sFmoZU'




bad = False
loop = None

client = discord.Client()


def lastWord(string): #yes i took this from geeksforgeeks i dont care

    lis = list(string.split(" "))


    length = len(lis)


    return lis[length - 1]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')










@client.event
async def on_message(message):



    if message.content == '?help':
        embed = discord.Embed(title="Funny Server Bot (1.2)", description="A bot made by Giddy#6129", color=0x00ff00)
        embed.add_field(name="?help", value="shows this menu", inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('?tts'):
        global vc
        voice_state = message.author.voice

        if voice_state is None:
            return await message.channel.send('```You need to be in a voice channel to use this command```')

        command = message.content.replace('?tts','')
        if command == '':
            await message.channel.send("```I Can't Say Nothing```")
        else:
            await message.channel.send((f'```Saying: {command}```'))
            engine = pyttsx3.init()


            filename = f'tts-audio/{random.randint(0, 1000000)}.mp3'

            engine.save_to_file({command} ,filename)



            engine.runAndWait()

            channel = client.get_channel(958021288482439222)
            try:
                vc = await channel.connect()
            except discord.errors.ClientException:
                print('Already In Voice Channel Ignoring')
            vc.play(discord.FFmpegPCMAudio(filename), after=lambda e: print('done', e))

    if message.content.startswith('?customtts'):
        file = random.randint(1,100000)
        arguments = message.content.replace('?customtts','')


        voice_state = message.author.voice

        if voice_state is None:
            return await message.channel.send('```You need to be in a voice channel to use this command```')

        if  arguments.replace(lastWord(arguments) ,'')=='':
            await message.channel.send("```I Can't Say Nothing```")
        else:
            await message.channel.send((f'```Saying: {lastWord(arguments)} as {arguments.replace(lastWord(arguments),"")}```'))
            ducky.speak( arguments.replace(lastWord(arguments) ,''), lastWord(arguments), file_path=f'uberduck/{file}.mp3')



            channel = client.get_channel(958021288482439222)


            try:
                vc = await channel.connect()
            except discord.errors.ClientException:
                print('Already In Voice Channel Ignoring')
            vc.play(discord.FFmpegPCMAudio(f'uberduck/{file}.mp3'), after=lambda e: print('done', e))

    if message.content.startswith('?newvoice'):
        voice = message.content.replace('?newvoice','')


        if voice not in voices:
            print(f'{voice} Is Not A Voice')
        else:
            with open('voice', "w") as f:
                f.write(voice)





    if message.content == '?listvoices':
        global voices_message
1
        await message.reply('Check Your Dms :wink:')



        for voice in sorted(voices): # sorting the voice list in alphabetical order
                voices_message = voices_message + f'{voice}\n'

        await message.reply(voices_message)





client.run(TOKEN)