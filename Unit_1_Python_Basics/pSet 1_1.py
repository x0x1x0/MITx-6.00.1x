"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
"""


# instead of following if call, i used a defined list of vowels to call from.
# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':

s = 'Kiara'
vowels = 0
vowel = ["a", "e", "i", "o", "u"]

for char in s:
    if char in vowel:
        vowels += 1
print('Number of vowels: ' + str(vowels)) 