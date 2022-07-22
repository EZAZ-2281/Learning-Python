from random import randint #, random

for x in range(1, 6):
    guessNumber = int(input("Enter a number from 1 to 5: "))
    randomNumber = randint(1, 5)
    #randomNumber = random.random() * 100

    if(guessNumber == randomNumber):
        print("won")
    else:
        print("You've lost")
        print("Random number is: ", randomNumber)
