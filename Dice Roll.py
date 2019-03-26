#imported the random module in order to use the method function .randint()
import random
#dice roll function
def dice_roll():
    print("-Dice Roll Simulator-")
    print("-Answer yes or no-")
    q = ""
    #the "q" variable uses an input function to ask player to roll dice.
    while q != "yes" or q != "no":
        q = input("Would you like to roll the dice? ")
        if q == "yes" or q == "no":
            break
    # Use a while loop to ask player if they would like to play again and repeat the process
    while True:
        dice = random.randint(1,6)
        if q == "yes":
            print("You rolled a "+str(dice)+".")
            replay = input("Would you like to roll again? ")
            if replay == "no":
                print("Goodbye!")
                break
        elif q == "no":
            print("See you again real soon!")
            break


#Calling the dice_roll() function
dice_roll()
