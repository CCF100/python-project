# imports libraries we will use
import time
import random
# sets values we will use later
number = 0
phrase = "The quick, brown, fox jumped over the lazy dog"

# calculates amount of letters in phrase (including spaces)
amount = len(phrase)
print("The current phrase has", amount, "letters")
# prints phrase
print("the phrase is", phrase)
print('begin loop')
time.sleep(1)

# prints phrase letters
for number in range(amount):
	print(number, phrase[number], end='\r')
	time.sleep(0.1)

# prints phrase letters in random order
print('\n')
print("Now, in random order!")
time.sleep(1)
for number in range(amount):
	exec('iteration = random.randint(0,amount - 1)')	
	print(number, phrase[iteration], "iteration", iteration, end='\r')
	time.sleep(0.1)
