import random
tries = 1
r = random.randint
surrender = 4
done = 7

# I'll put a code for music to be playing in the backround of the game here

D = str(input("Select difficulty mortal. [easy/med/hard]"))
# Sets Variable for max tries 'done' offering 'surrender' the random number and how many tries your on 'tries'
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
# Allows user to set difficult and mocks them appropriately
while G != r:
    if G > r:
        print("Has aiming high ever worked for you.... really?")
        G = int(input("Keep trying...."))
        tries = tries + 1
    elif G < r:
        print("Maybe you should have higher aspirations in life.")
        G = int(input("Try again....."))
        tries = tries + 1
        # Lets user know to guess higher or lower and adds to the 'tries' with every incorrect guess
    if tries == surrender:
        R = str(input("Are you ready to admit my superior intellect?"))
        if R == "no":
            print("Ill just sit here well you bang on your keyboard like a chimp then")
        elif R == "yes":
            print("This is why computers will take over the world!")
            break
            # Allows user to surrender after 4 guesses
    if tries == done:
        if G == r:
            print("I would congratulate you, but even a broken clock is right twice a day.")
            print("I mean come on, it took you", tries, "guesses!")
        else:
            print("This is why computers will take over the world")
            exit()
            # This section deal with the end of the game, either you win and it mocks you, you lose and it mocks you