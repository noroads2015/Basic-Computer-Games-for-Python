import random,shutil
columns, rows = shutil.get_terminal_size()

print ("Acey Ducey Card Game".center(columns))
print ("Adapted from original version BASIC Computer Games".center(columns))
print ("by David H. Ahl".center(columns))
print ("Python version by TomToad".center(columns))
print (
"""
Acey-Ducey is played in the following manner
The dealer (computer) deals two cards face up
You have an option to bet or not bet depending
on whether or not you feel the card will have
a value between the first two.
If you do not want to bet, input a 0
"""
)
stash = 100
cardNames = ["two","three","four","five","six","seven","eight",
             "nine","ten","Jack","Queen","King","Ace"]
while True:
    print ("you now have",stash,"dollars.\n")
    print ("here are your next two cards.")
    while True:
        carda = random.randrange(0,13)
        cardb = random.randrange(0,13)
        if cardb > carda:
            break

    print (cardNames[carda])
    print (cardNames[cardb])

    while True:
        try:
            bet = int(input("What is your bet? "))
        except ValueError:
            print ("Please enter a number")
        else:
            if bet > stash:
                print("Sorry, my friend, but you bet too much.")
                print("You only have",stash,"dollars to bet.")
                continue
            else:
                break

    if bet == 0:
        print ("Chicken!!\n")
        continue
    
    cardc = random.randrange(0,13)
    print (cardNames[cardc])

    if cardc > carda and cardc < cardb:
        print ("You win!!")
        stash += bet
    else:
        print ("Sorry, you lose!")
        stash -= bet

    if stash == 0:
        print ("Sorry, friend but you blew your wad.")
        response = input("Try again? (yes or no) ")
        if response.lower() != "yes": break
        stash = 100

print ("Ok, hope you had fun")


