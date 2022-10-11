"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

# letters can be compared by < > == etc.
# the 0 index of s is the first letter. 
# Therefore we start with a string at s[0]
# for every index in s we check wether the letter at the indexed position
# is alphabetically "greater or equal" to the previous.

# if that is the case we add that letter to our temporary string
# now, if our tempstring is longer than the longest string recorded so far
# we set our longest_yet to be the length of the tempstring
# and let our tempstring sit in place of the longest_total
# which will sit in place until a new longer tempstring takes its place.
# we now increase our index by one, to move to the next letter.

# if our letter is not greater or equal to the previous
# we simply make the tempstring be the next letter up and start again
# this also resets the tempstring if the following letter
# is not in alphabetical order.

s = "hellygreiftdenkederan"
   
longest_yet = 0 
tempstring = s[0]
longest_total = s[0]

for i in range(len(s)-1):
	if s[i+1] >= s[i]:
		tempstring += s[i+1]
		if len(tempstring) > longest_yet:
			longest_yet = len(tempstring)
			longest_total = tempstring
	else:
		tempstring = s[i+1]
	i += 1
 
print("The longest substring in alphabetical order is: " + longest_total)