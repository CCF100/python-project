#Let's first check if this script is being run by a frontend or not
print("__name__ is set to", __name__)
if __name__ == '__main__':
	print("This script isn't ment to be run by itself! Please run it with either connect4-2D or 3D!")
#Import libraries
from termcolor import colored
#Versioning info
print(colored("<<connectCore.", 'red')+colored("p", 'blue')+colored("y", 'yellow'), colored("- Written by Caleb Fontenot>>", 'red'))
print("~~Experimental Version~~"+'\n')
#setup grid dict
grid = {(i, j): None for i in range(7) for j in range(6)}
#manipulating red
#grid[0, 3] = 'red'
