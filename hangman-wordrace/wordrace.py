import random, sys, os
colors = {"black":"\033[1;30;40m",
          "blue":"\033[1;34;40m",
          "green":"\033[1;32;40m",
          "cyan":"\033[1;36;40m",
          "red":"\033[1;31;40m",
          "purple":"\033[1;35;40m",
          "yellow":"\033[1;33;40m",
          "white":"\033[1;37;40m",
          "reset":""}
    
def changeColor(color):
    print(colors[color],end="")
            
def replaceWithMask(word, hidden, guess):
    guessedLetters = 0
    for index in range(0,len(word)):
        if word[index] == guess:
            hidden = hidden[:index]+guess+hidden[index+1:]
            guessedLetters += 1
    return (hidden, guessedLetters)

def drawRaceCars(carA, carB):
    car = "`o##o>"
    changeColor("red")
    print(f"\n\n{'_'*carA}{car}{'_'*(20-carA)}|")
    changeColor("green")
    print(f"{'_'*carB}{car}{'_'*(20-carB)}|")
    changeColor("blue")
    

def game(word, hidden, tries):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettersUsed = "--------------------------"
    totalGuessed = 0

    while tries > 0:
        drawRaceCars((10-tries)*2, int(totalGuessed / len(word) * 20))
        print(f"Letters used\n{lettersUsed}\n")
        print(f"{hidden} {tries}")
        guess = input("What is your guess? ").upper()
        if guess in letters:
            if guess in lettersUsed:
                print(f"{guess} has already been used")
            else:
                index = ord(guess) - 65
                lettersUsed = lettersUsed[:index]+guess+lettersUsed[index+1:]
                if guess in word:
                    hidden, guessed = replaceWithMask(word, hidden, guess)
                    totalGuessed += guessed
                    if hidden == word:
                        drawRaceCars((10-tries)*2,20)
                        return True
                else:
                    print(f"{guess} is not in the word!")
                    tries -= 1
        else:
            print("Please enter a single letter A-Z")

    drawRaceCars(20, int(totalGuessed / len(word) * 20))
    return False

def main():
    with open("words.txt") as f:
        words = [w.strip().upper() for w in f.read().split("\n") if len(w) >= 5]

    while True:
        tries = 10
        word = random.choice(words)
        hidden = "-"*len(word)
        result = game(word, hidden, tries)
        if result == True:
            print(f"{word} You won the race!!!")
        else:
            print(f"{word} Sorry, you lost!")
        again = input("Play again? (Y/N): ").upper()
        if "Y" not in again:
            break

if sys.platform.startswith("win"):
    os.system("color")

main()
