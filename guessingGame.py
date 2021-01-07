# guessingGame
#One version of a random number guessing game program in python

import random
tries = 1
r = random.randint
surrender = 4
done = 7
#Sets variable for amount of tries, the random number, and tries allowedtill surrender is offered and your forced out
D = str(input("Select difficulty mortal. [easy/med/hard]"))
if D == "easy":
    r = random.randint(1, 100)
    print("Figures. Choose a number between 1 and 100")
if D == "med":
    r = random.randint(1, 1000)
    print("feeling brave today? Choose a number between 1 and 1000")
if D == "hard":
    r = random.randint(1, 1000000)
    print("Someone has a death wish. Choose a number between 1 and 1,000,000")
G = int(input(""))
#Sets the difficulty setting off input from the user
while G != r:
    if G > r:
        print("Has aiming high ever worked for you.... really?")
        G = int(input("Keep trying...."))
        tries = tries + 1
    elif G < r:
        print("Maybe you should have higher aspirations in life.")
        G = int(input("Try again....."))
        tries = tries + 1
    if tries == surrender:
        R = str(input("Are you ready to admit my superior intellect?"))
        if R == "no":
            print("Ill just sit here well you bang on your keyboard like a chimp then")
        elif R == "yes":
            print("This is why computers will take over the world!")
            break
    if tries == done:
        if G == r:
            print("I would congratulate you, but even a broken clock is right twice a day.")
            print("I mean come on, it took you", tries, "guesses!")
        else:
            print("This is why computers will take over the world")
            exit()
