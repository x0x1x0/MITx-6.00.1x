"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2
"""


s = "aboboabboboaboabboobaobaobboabobobobobo"
timesofbob = 0
name = "bob"



for i in range(len(s)):
    if s[i:i+3] == "bob":
        timesofbob += 1
print("Number of times " + str(name) + " occurs is: " + str(timesofbob))

