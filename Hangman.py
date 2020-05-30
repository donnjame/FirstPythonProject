'''
Hangman Game
First Ever Python code

'''

myword = input("Your Word: ")
hiddenword = []
wrongguess =[]
myword = myword.lower()
for letter in myword:
    hiddenword.append(letter)
reveal = hiddenword.copy()
for i in range (len(reveal)):
    reveal[i]= '*'

win = all(elem in reveal for elem in hiddenword)

while len(wrongguess) != 6:
    win = all(elem in reveal for elem in hiddenword)
    if win == True:
        print('congratulations, {} is the secret word, you win!'.format(myword))
        break
    guess = input('guess a letter')
    revealed = [pos for pos,char in enumerate(myword) if char == guess]
    if guess in hiddenword:
        for item in revealed:
            reveal[item] = guess
        print(reveal)
    else:
        wrongguess.append(guess)
        if len(wrongguess) < 6:
            print('Incorrect, try again') 
            print("You have {} guesses remaining".format(6-(len(wrongguess))))
        
            
else:
    print('Game over you lose!')