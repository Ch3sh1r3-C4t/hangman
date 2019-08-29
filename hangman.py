word = input("insert word to guess: ")
unkownWord = "_" * len(word)
unkownWord = list(unkownWord)
usedLetter = [""]
guesses = 6
presentInList = False
answer = ""


def listToString(s):
    # initialize an empty string
    str1 = ""
    # return string
    return (str1.join(s))


while guesses > 0:
    letter = input("insert letter:")
    # try condition better
    if letter in usedLetter:
        print("letter already used, please choose other")
        letter = input("insert letter:")
    else:
        for i in range(len(unkownWord)):
            if letter == word[i]:
                unkownWord[i] = letter
                presentInList = True
            else:
                pass
        if presentInList is not True:
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
        presentInList = False
    answer = listToString(unkownWord)
    if answer == word:
        print("congratulation you found the word!")
        break
    else:
        print(answer)
        usedLetter.append(letter)
