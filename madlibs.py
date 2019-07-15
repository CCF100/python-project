# Toggle me for debugging
debug = 1

# Import the libraries we will use
import re
import sys
import random
import platform
import argparse
# check to see if termcolor is installed, we need it for color to xwork
try:
	from termcolor import colored
except ImportError:
	print("termcolor is not installed! Please install termcolor with" '\n', '\n', "pip install termcolor", '\n','\n'+"Note: You may need to run pip as root")
	exit()
if debug == 1: 
	print("termcolor is installed!")
# If we are on Windows, we need to do a little more to get color to work
if platform.system() == 'Windows':
	import os
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
	f = open('storyCount.txt', 'w')
	f.write(StoryCount)
	f.close()
	exit()
	print("Writing", StoryCount, "to txt file!")
if args.setup == True:
	sys.exit("If you want to include your own MadLibs story, you need to do the following:"+'\n')
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
# Count stories

# Randomly pick what story we will use
story = random.randint(1, IntStoryCount)

# Alright, let's get the data from stories.txt
f = open('stories.txt', 'r')
# This pulls the title from stories.txt
storyName = f.readline()
# This pulls the story from stories.txt
storyContent = f.readline()
# todo: remove characters from story identifier and make every even number be recognized as a story, and every odd as it's title


# Hacky shenanigans
#selectedStoryName = storyName[story - 1]

# Print current story title
print("Current story title is", '"'+storyName+'"')

# Alright, now onto the tricky part. We need to filter out all of the bracketed words in stories.txt, putting them into a list, replacing them with incremental strings. We also need to count how many there are for later.
# Pull all of the items with the <> brackets
filtered = re.findall(r'<.*?>', storyContent)
filteredReplaced = re.sub(r'<.*?>', storyContent)
# We got them!
print(filtered)
# Now we need to count them
replacedNumber = len(filtered)
print(replacedNumber)






