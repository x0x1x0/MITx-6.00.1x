


print("Please think of a number between 0 and 100!")
low = 0
high = 100
i = 0
while i in range(0,100):
	guess = int((low + high)/2)
	print("Is your secret number" + " " + str(guess) + "?")
	response = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly."))
	if response == 'h':
		high = guess
		guess = int((low+high)/2)
		
	elif response == 'l':
		low = guess
		guess = int((low+high)/2)

	elif response == 'c':
		break

	else:
		print("Enter only c or h or l")
print("Game over. Your secret number was:" + " " + str(guess))