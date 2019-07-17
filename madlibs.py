# Toggle me for debugging
debug = 1

# Import the libraries we will use
from datetime import datetime
import re
import sys
import random
import platform
import argparse
import os
# check to see if termcolor is installed, we need it for color to work
try:
	from termcolor import colored
except ImportError:
	print("termcolor is not installed! Please install termcolor with" '\n', '\n', "pip install termcolor", '\n','\n'+"Note: You may need to run pip as root")
	exit()
if debug == 1: 
	print("termcolor is installed!")
# If we are on Windows, we need to do a little more to get color to work
if platform.system() == 'Windows':
	os.system('color')
# ArgSparce
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--setup", help="Explains how to setup .txt file", action="store_true")
parser.add_argument("-c", "--story", type=int, help="Write story count to file")
args = parser.parse_args()
# convert the integer to a string because pickiness
StoryCount = str(args.story)

#if statements for ArgSparce

# line 36 fails if args.story reads as "None", so we need to clear that string if it reads as such.
if args.story == None:
	exec('args.story = int(0)')
# args.story should now read as 0
if args.story > 0:
	f = open('storyCount.txt', "r+")
	IntStoryCount = f.read()
	print("There are currently", IntStoryCount, "in stories.txt")	
	f.seek(0)	
	f.write(StoryCount)
	f.close()
	print("Writing", StoryCount, "to txt file!")
	exit()
if args.setup == True:
	sys.exit("If you want to include your own MadLibs story, you need to do the following:"+'\n'+"1. Open "+"\"stories.txt\""+'\n'+"2. Put the title of the story on all of the odd lines"+'\n'+"3. Put the entire story on one line, and put words you wish to replace in <>. Use the example as a reference."+'\n'+"4. When you are done, run me with the -c or --story flag to update how many stories are in stories.txt.")
# Linux easter egg
if platform.system() == 'Linux':
	print('Linux master race! XD')
# Introduce yourself
print (colored("<<madlibs.", 'red')+colored("p", 'yellow')+colored("y", 'blue'), colored("- Written by Caleb Fontenot>>", 'red'), '\n' "Project started on July 13, 2019")
print("I pull txt files in the directory you place me in for stories!" '\n' '\n' "Run me with the --setup flag for instructions on setting a story up!" '\n')

# Notify if verbose
if debug == 1:
	print("Debug mode is enabled! Being verbose!", '\n')
else:
	print('\n')
# Now on to business!
# Load files
f = open('storyCount.txt', 'r')
StoryCount = f.read()
IntStoryCount = int(StoryCount)
print("Detected", IntStoryCount, "stories")
# Randomly pick what story we will use
story = random.randint(1, IntStoryCount)

# Alright, let's get the data from stories.txt
i = 1
f = open('stories.txt', 'r')
for line in f.readlines():
	if i % 2 == 0 :
		storyContent = line
	else:
		storyName = line
	i+=1
f.close()
# Print current story title, but remove the brackets first
filteredTitle = re.findall(r'<(.*?)>', storyName)
# print the first result
print("Current story title is", '"'+filteredTitle[0]+'"','\n')

# Alright, now onto the tricky part. We need to filter out all of the bracketed words in stories.txt, putting them into a list, replacing them with incremental strings. We also need to count how many there are for later.
# Pull all of the items with the <> brackets
filtered = re.findall(r'<(.*?)>', storyContent)
# We got them!
if debug == 1:
	print(filtered, '\n')
# Now we need to count them
replacedNumber = len(filtered)

# Run a loop to get the words

replaceList = []
#replaceList =['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
replaceList.append("")
print("Type a noun, verb, adjective, or adverb depending on what it asks you, followed by enter.", '\n')

for loopCount in range(replacedNumber):
	replaceVar = input("Give me a(n) "+colored(filtered[loopCount], 'blue')+": ")
	replaceList.append(replaceVar)
print(replaceList)
# Run a loop to replace the words

print("Replacing Words...")

# Split the Story Content into a list
storyContentList = re.split(r'<.*?>', storyContent)
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
#for loopCount in range(storyContentCount):
#	#print(storyContentList[loopCount])
#	storyContentListColored[x-1] = '\"'+re.escape(storyContentListColored[x-1])+'\"'
#	storyContentListColored.insert(x, "colored(\'"+replaceList[loopCount]+"\', '"\'+blue+"\""),")
#	x = x+2
#print(storyContentListColored)
#print('\n')
# Merge lists into a string
generatedStory = ""
generatedStory = generatedStory.join(storyContentList)
# for the colored printout...
#generatedStoryColored = ""
#generatedStoryColored = generatedStoryColored.join(storyContentListColored)
#print(generatedStoryColored)
print(generatedStory)
#print(exec(generatedStoryColored))
#exit()
#Alright! We're done! Let's save the story to a file
now = datetime.now()

if os.path.exists("saved stories"):
	pass
else:
	os.system("mkdir \"saved stories\"")

currentDate = now.strftime("%d-%m-%Y-%H:%M:%S")
saveFile = 'saved stories/generatedStory-'+currentDate+'.txt'
print("Saving story to .txt file")
file = open(saveFile, 'w+')

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
