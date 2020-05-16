Word Race is a variation of the game Hangman.  I decided to make the game
with racecars instead of a hanging man in order to avoid the complexities
of drawing the hanging man and gallows.  Also, it removes the more macabre
part of the game so it can be more appealing to younger players.

The goal of the game is the same, try and guess the word letter by letter.
Every time you guess a correct letter, your racecar moves forward.  Every
time you guess a wrong letter, the opponent's racecar moves forward.  First
to the finish line wins.

words.txt is the same as pocket.txt from
https://web.archive.org/web/20120420170337/http://www.puzzlers.org/pub/wordlists/pocket.txt
modified by removing all words less than 5 letters long.

The code uses ANSI escape codes to change the colors of the text.  If you see
a bunch of random characters and numbers, such as ?[1;32;40m, then just remark
out the changeColor() calls in lines 25, 27, and 29.  Then the code should 
work ok without changing colors.
