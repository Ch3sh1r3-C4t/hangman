# word inputted
word = input("insert word to guess: ")
# variables for word to find
unkownWord = "_" * len(word)
unkownWord = list(unkownWord)
presentInUnkownWord = False
# variable for the letter used and anwer
usedLetter = [""]
answer = ""
# number of guesses
guesses = 6


def listToString(s):
    # initialize an empty string
    str1 = ""
    # return string
    return (str1.join(s))


while guesses > 0:
    print(listToString(unkownWord))
    letter = input("insert letter or word:")
    # try condition better
    if letter in usedLetter:
        print("letter already used, please choose other")
        letter = input("insert letter:")
    elif letter == word:
        print("congratulation you found the word!")
        break
    else:
        for i in range(len(unkownWord)):
            if letter == word[i]:
                unkownWord[i] = letter
                presentInUnkownWord = True
            else:
                pass
        if presentInUnkownWord is not True:
            guesses -= 1
            if guesses == 5:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" |    ")
                print("_|_   ")
            elif guesses == 4:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" |  | ")
                print("_|_   ")
            elif guesses == 3:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" | /| ")
                print("_|_   ")
            elif guesses == 2:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" | /|\\")
                print("_|_   ")
            elif guesses == 1:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" | /|\\")
                print("_|_/")
            elif guesses == 0:
                print("%d guesses remaining" % (guesses))
                print(" ____ ")
                print(" |  | ")
                print(" |  O ")
                print(" | /|\\")
                print("_|_/\\")
                print("The correct word was: %s" % (word))
        presentInUnkownWord = False
    answer = listToString(unkownWord)
    if answer == word:
        print("congratulation you found the word!")
        break
    else:
        usedLetter.append(letter)
