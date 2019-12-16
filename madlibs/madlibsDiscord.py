#!/usr/bin/python
# Toggle me for debugging
debug = 1

# Import the libraries we will use
from datetime import datetime
from gtts import gTTS
import discord
import re
import sys
import random
import os
import asyncio

async def gameLoop():

# convert the integer to a string because pickiness
	StoryCount = str(args.story)

	#if statements for ArgSparce
	
	# line 36 fails if args.story reads as "None", so we need to clear that string if it reads as such.
	if args.story == None:
		exec('args.story = int(0)')
	# Introduce yourself
	await channel.send("<<madlibsDiscord.py - Written by Caleb Fontenot>>") 
	await channel.send("Initial project started on July 13, 2019")
	await channel.send("Discord Bot started on December 16, 2019")
	# Notify if verbose
	if debug == 1:
		await channel.send("Debug mode is enabled! Being verbose!")
	# Now on to business!
	exit()
	# Load files
	f = open('storyCount.txt', 'r')
	StoryCount = f.read()
	IntStoryCount = int(StoryCount)
	await channel.send("Detected "+IntStoryCount+" stories")
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
	print(storyNameStr)
	# Print current story title, but remove the brackets first
	filteredTitle = re.findall(r'<(.*?)>', storyNameStr[story-1])
		
	# print the first result
	print("Current story title is", '"'+filteredTitle[0]+'"','\n')
# Alright, now onto the tricky part. We need to filter out all of the bracketed words in stories.txt, putting them into a list, replacing them with incremental strings. We also need to count how many there 	are for later.
# Pull all of the items with the <> brackets
	filtered = re.findall(r'<(.*?)>', storyContentStr[story-1])
	# We got them!
	if debug == 1:
		print(filtered, '\n')
	# Now we need to count them
	replacedNumber = len(filtered)
	
	# Run a loop to get the words
	
	replaceList = []
	#replaceList =['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', 	'17', '18', '19', '20', '21', '22', '23', '24']
	replaceList.append("")
	print("Type a noun, verb, adjective, or adverb depending on what it asks you, followed by enter.", '\n')
	
	for loopCount in range(replacedNumber):
		replaceVar = input("Give me a(n) "+colored(filtered[loopCount], 'blue')+": ")
		replaceList.append(replaceVar)
	print(replaceList)
# Run a loop to replace the words

	print("Replacing Words...")
	
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
	storyContentListColored = re.split(r'<.*?>', storyContent)
	x = 0

	# Merge lists into a string
	generatedStory = ""
	generatedStory = generatedStory.join(storyContentList)

	print(generatedStory)
	#exit()
	#Alright! We're done! Let's save the story to a file
	now = datetime.now()

	if os.path.exists("saved stories"):
		pass
	else:
		os.system("mkdir \"saved stories\"")
		currentDate = now.strftime("%d-%m-%Y-%H:%M:%S")
		saveFile = 'saved stories/generatedStory-'+currentDate
	print("Saving story to .txt file")
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
#Setup Discord functions and announce on discord that we are ready
class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)
		channel = client.get_channel(656233549837631508)
		await channel.send("madlibs.py - Discord Edition has successfully connected!")
		await channel.send("Run `mad!start` to start a a game")
		print("Ready!")		
	async def on_message(self, message):
		if message.content == 'mad!start':
			await asyncio.set_event_loop(gameLoop())

#Run main Game loop


# Connect Bot To Discord and start running
client = MyClient()
client.run('')
exit()


	# say the tts
	#print('\n'+"Processing Text-To-Speech, please wait..."+'\n')
	#tts = gTTS(text=generatedStory+"This story was generated by Caleb Fontenot's MadLibs.py", lang='en')
	#tts.save("TTS.mp3")
	##os.system("play TTS.mp3")
	#os.system("mv TTS.mp3 "+"\""+saveFile+".mp3"+"\"")
	#Start Discord Bot loop