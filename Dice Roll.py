#imported the random module in order to use the method function .randint()
import random
#dice roll function
def dice_roll():
	print("-Dice Roll Simulator-")
	print("-Answer yes or no-")
	#the "q" variable uses an input function to ask player to roll dice.
	q = input("Would you like to roll the dice? ")
	# Use a while loop to ask player if they would like to play again and repeat the process
	while True:
		dice = random.randint(1,6)
		if q == "yes":
			print("You rolled a "+str(dice)+".")
			replay = input("Would you like to roll again? ")
			if replay == "no":
				break
		elif q == "no":
			break


#Calling the dice_roll() function
dice_roll()
