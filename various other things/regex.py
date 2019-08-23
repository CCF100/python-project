# import re library
import re

# Here's our string
lol = "Lol this is a string"
print(lol)

# now let's filter out the word "string"
p = re.compile('string')

filtered = p.match('string')

print(filtered)



