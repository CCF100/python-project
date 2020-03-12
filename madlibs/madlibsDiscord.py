#!/usr/bin/python
# Toggle me for debugging
debug = 1
# Displays warning message
testing = 1
# Import the libraries we will use
#from mega import Mega
from datetime import datetime
from gtts import gTTS
import discord
import re
import sys
import random
import os
import asyncio
import ffmpeg
#import talkey

async def gameLoop():
    # In the future we will detect what channel we were summoned in, but for now:
    ativeChannel = 656233549837631508
    #Init tts, and connect voice to channel, reinit connection if broken
    voiceChannel = client.get_channel(682688245964079127)
    voice = await voiceChannel.connect()
    if voice.is_connected() == True:
        await voice.disconnect()
    voice = await voiceChannel.connect()
    # Set bot presence
    await client.change_presence(activity=discord.Game(name='madlibs.py'))
    # Introduce yourself
    channel = client.get_channel(656233549837631508)
    await channel.send("**<<madlibsDiscord.py <:python:656239601723113472> - Written by Caleb Fontenot>>**") 
    await channel.send("Initial project started on **July 13, 2019**")
    await channel.send("Discord Bot started on **December 16, 2019**")
    # Notify if verbose
    if debug == 1:
        await channel.send("Debug mode is enabled! Being verbose!")
    # Now on to business!
    # Load files
    async with channel.typing():	
        f = open('storyCount.txt', 'r')
        StoryCount = f.read()
        IntStoryCount = int(StoryCount)
        await channel.send("Detected "+str(IntStoryCount)+" stories")
    # Randomly pick what story we will use
    story = random.randint(1, IntStoryCount)
    
    #Declare vars
    storyContentStr = []
    storyNameStr = []
    # Alright, let's get the data from stories.txt
    i = 1
    f = open('stories.txt', 'r')
    for line in f.readlines():
        if i % 2 == 0 :
            storyContent = line
            storyContentStr.append(storyContent)	
        else:
            storyName = line
            storyNameStr.append(storyName)
        i+=1
    f.close()
    await channel.send(storyNameStr)
    # Print current story title, but remove the brackets first
    filteredTitle = re.findall(r'<(.*?)>', storyNameStr[story-1])
        
    # print the first result
    await channel.send("Current story title is  "+'"'+str(filteredTitle[0])+'"'+'\n')
# Alright, now onto the tricky part. We need to filter out all of the bracketed words in stories.txt, putting them into a list, replacing them with incremental strings. We also need to count how many there 	are for later.
# Pull all of the items with the <> brackets
    filtered = re.findall(r'<(.*?)>', storyContentStr[story-1])
    # We got them!
    if debug == 1:
        await channel.send(str(filtered))
    # Now we need to count them
    replacedNumber = len(filtered)
    
    # Run a loop to get the words
    
    replaceList = []
    #replaceList =['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    replaceList.append("")
    await channel.send(str("Type a noun, verb, adjective, or adverb depending on what it asks you, followed by enter."))
    
    for loopCount in range(replacedNumber):
        print("Times looped: "+str(loopCount))
        #Wait for user to reply
        await channel.send("Give me a(n) "+"**"+str(filtered[loopCount])+"**"+": ")	
            #if we see our own message, ignore it
        async def on_message(message):
            if message.author == self.user:
                return
            #if we see a message in a channel that isn't in the active one, ignore it
            if message.channel.id != activeChannelID:
                return
        # Push text to gTTS and save it to a file
        tts = gTTS(text="Give me a(n) "+str(filtered[loopCount])+": ")
        os.system("rm badCurrentTTS.mp3")
        os.system("rm currentTTS.wav")
        tts.save("badCurrentTTS.mp3")
       # gTTS is stupid and gives us a file that discord.py doesn't understand, so we have to convert it
        (
            ffmpeg
            .input('badCurrentTTS.mp3')
            .output('currentTTS.wav', audio_bitrate=48000, format='wav', sample_fmt='s16', ac='2')
            .run()
        )
        if voice.is_playing() == True:
            print("Audio is playing! Stopping playback!"+'\n')
            voice.stop()
        print("Attempting to play audio"+'\n')
        voice.play(discord.FFmpegPCMAudio("currentTTS.wav"))
        raw_message = await client.wait_for('message')
        replaceVar = raw_message.content
        print("You gave me: "+replaceVar)
        replaceList.append(replaceVar)
    print(replaceList)
# Run a loop to replace the words

    await channel.send("Replacing Words...")
    
    # Split the Story Content into a list
    storyContentList = re.split(r'<.*?>', storyContentStr[story-1])
    # Count the items in the list
    storyContentCount = len(storyContentList)
    x = 0
    for loopCount in range(storyContentCount):
        #print(storyContentList[loopCount])
        storyContentList.insert(x, replaceList[loopCount])
        x = x+2
    # To get colored words for our output, we need to add the appropiate commands to our variable.
    x = 0

    # Merge lists into a string
    generatedStory = ""
    generatedStory = generatedStory.join(storyContentList)
# Determine file name for file output
    now = datetime.now()
    currentDate = now.strftime("%d-%m-%Y-%H:%M:%S")
    saveFile = 'saved stories/generatedStory-'+currentDate
# Send Story to Discord
    await channel.send(generatedStory)
    await channel.send("Processing TTS, please wait!")
    async with channel.typing():
        tts = gTTS(text=generatedStory+"This story was generated by CCF_100's MadLibs.py", lang='en')
        os.system("rm badCurrentStory.mp3")
        tts.save("badCurrentStory.mp3")
        # gTTS is stupid and gives us a file that discord.py doesn't understand, so we have to convert it
        (
            ffmpeg
            .input('badCurrentStory.mp3')
            .output(saveFile+'.mp3', audio_bitrate=48000, format='wav', sample_fmt='s16', ac='2')
            .run()
        )
        if voice.is_playing() == True:
            print("Audio is playing! Stopping playback!"+'\n')
        voice.stop()
        print("Attempting to play audio"+'\n')
        voice.play(discord.FFmpegPCMAudio(saveFile+".mp3"))
    #exit()
    #Alright! We're done! Let's save the story to a file
    if os.path.exists("saved stories"):
        pass
    else:
        os.system("mkdir \"saved stories\"")    
    print("Saving story to .txt file")
    await channel.send("Saving story to .txt file")
    async with channel.typing():
        file = open(saveFile+'.txt', 'w+')	 
        line_offset = []
        offset = 0
        for line in file:
            line_offset.append(offset)
            offset += len(line)
        file.seek(0)
        file.write(filteredTitle[0]+'\n'+'\n')
        file.write(generatedStory)
        file.write('\n'+"Generated by Caleb Fontenot\'s madlibs.py")
        file.close()
    #Send generated .txt file to Discord
    await channel.send("Sending .txt file...")
    discordFile = discord.File(saveFile+'.txt', filename="generatedStory.txt")
    await channel.send(file=discordFile)
    #Send generated .mp3 file to Discord
    mp3File = saveFile+'.mp3'
    def file_size(fname):
        statinfo = os.stat(fname)
        return statinfo.st_size
    print("MP3 is "+str(file_size(mp3File))+" bytes.")
    await channel.send("Converted WAV is "+str(file_size(mp3File))+" bytes.")
    if int(file_size(mp3File)) <= int(8389999):
        # File is over 8 MiB! This will fail if we send the file corrected for transmission via Discord's voice chat. Let's send the original instead.
        discordFile = discord.File("badCurrentStory.mp3", filename=saveFile+'.mp3')
        await channel.send(file=discordFile)
    else:
        discordFile = discord.File(saveFile+'.wav', filename=saveFile+'.wav')
        await channel.send(file=discordFile)

async def messageListening():
    messagesList = []
    messageAuthorList = []
    class infinite:
        while True:
            x = 0
            async def on_message(self, message, pass_context=True):
                messageList.append(message.content)                
                messageAuthorList.append(message.author)
                print("Message from", messageAuthorList[x], messagesList[x])
                x + 1
    infinite()
#Setup Discord functions and announce on discord that we are ready

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        channel = client.get_channel(656233549837631508)
        await channel.send("madlibs.py - Discord Edition has successfully connected!")
        if testing == 1:
            await channel.send("This bot is currently being worked on! Please don't start a game!")
        await channel.send("Run `mad!start` to start a a game")
        print("Ready!")		
    async def on_message(self, message, pass_context=True):
        if message.content == 'mad!start':
            channel = client.get_channel(656233549837631508)			
            await gameLoop()
            await channel.send("Done!")
    async def on_message(self, message, pass_context=True):
        if message.content == 'mad!testMessages':
            channel = client.get_channel(656233549837631508)
            await channel.send("Listening to messages, logging time difference...")
            await messageListening()
        
  #Disconnect Voice
            await asyncio.sleep(60)
            voiceChannel = client.get_channel(682688245964079127)
            await voice.disconnect()

#Run main loop
# The Discord bot ID isn't stored in this script for security reasons, so we have to go get it
f = open('botID.txt', 'r')
BotID = f.read()
#Cleanup from previous session
#os.system("rm badCurrentTTS.mp3")
#os.system("rm currentTTS.wav")
# Connect Bot To Discord and start running
client = MyClient()
client.run(BotID)
exit()


	# say the tts
	#print('\n'+"Processing Text-To-Speech, please wait..."+'\n')
	#tts = gTTS(text=generatedStory+"This story was generated by Caleb Fontenot's MadLibs.py", lang='en')
	#tts.save("TTS.mp3")
	##os.system("play TTS.mp3")
	#os.system("mv TTS.mp3 "+"\""+saveFile+".mp3"+"\"")
	#Start Discord Bot loop
