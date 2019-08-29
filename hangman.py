import os


class Error(Exception):
            """Base class for other exceptions"""
            pass


class LetterAlreadyUsed(Error):
                """Raised when the letter/word is already used"""
                pass


def listToString(s):
    # initialize an empty string
    str1 = ""
    # return string
    return (str1.join(s))


keepGoing = "Y"
# word inputted
word = input("insert word to guess: ")
os.system('clear')
# variables for word to find
unkownWord = "_" * len(word)
unkownWord = list(unkownWord)
presentInUnkownWord = False
# variable for the letter used and anwer
usedLetter = []
answer = ""
# number of guesses
guesses = 6

while guesses > 0:
    print(listToString(unkownWord))
    try:
        letter = input("insert letter or word:")
        if letter in usedLetter:
            print("letter/word already used, please choose other")
            letter = input("insert letter:")
    except LetterAlreadyUsed:
        print("letter/word already used, please choose other")
        letter = input("insert letter:")
    else:
        if letter == word:
            print(word)
            print("congratulation you found the word!")
            keepGoing = input("do you want to continue (Y,N)? ")
            if keepGoing == "Y":
                word = input("insert word to guess: ")
                os.system('clear')
                # variables for word to find
                unkownWord = "_" * len(word)
                unkownWord = list(unkownWord)
                presentInUnkownWord = False
                # variable for the letter used and anwer
                usedLetter = []
                answer = ""
                # number of guesses
                guesses = 6
            elif keepGoing != "Y" and keepGoing != "N":
                print("input not valid")
                break
            else:
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
                    keepGoing = input("do you want to continue (Y,N)? ")
                    if keepGoing == "Y":
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
                    elif keepGoing != "Y" and keepGoing != "N":
                        print("input not valid")
                        break
                    else:
                        print("thank for play")
                        break
            presentInUnkownWord = False
        answer = listToString(unkownWord)
        if answer == word:
            print(word)
            print("congratulation you found the word!")
            keepGoing = input("do you want to continue (Y,N)? ")
            if keepGoing == "Y":
                word = input("insert word to guess: ")
                os.system('clear')
                # variables for word to find
                unkownWord = "_" * len(word)
                unkownWord = list(unkownWord)
                presentInUnkownWord = False
                # variable for the letter used and anwer
                usedLetter = [""]
                answer = ""
                # number of guesses
                guesses = 6
            elif keepGoing != "Y" and keepGoing != "N":
                print("input not valid")
                break
            else:
                break
        else:
            usedLetter.append(letter)
