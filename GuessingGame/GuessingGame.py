from random import randrange

def userInputYesOrNo():
    answer = ""
    while (answer != "y" and answer != "n"):
        answer = input("Please input y for yes, n for no  ")
    return answer

def userInputLowOrHigh():
    answer = ""
    while (answer != "l" and answer != "h"):
        answer = input("please input l for low, h for high ")
    return answer

def guessingANumber(lowerBound, upperBound):
    return randrange(lowerBound, upperBound)

def playGuessingGame(lowerBoundInput, upperBoundInput):
    upperBound = upperBoundInput
    lowerBound = lowerBoundInput
    while (True):
        computerAnswer = guessingANumber(lowerBound, upperBound + 1)
        computerStoredAnswer = computerAnswer ##Remember the guess so it can change the bounds
        print("I am going to guess your number. Is it...", computerStoredAnswer, "?")
        playerAnswer = userInputYesOrNo()
        if (playerAnswer == "y"):
            break
        else:
            print("lower bound is", lowerBound, "upper bound is", upperBound)
            print("Is it too lower or too high?")
            playerAnswer = userInputLowOrHigh()
            if (playerAnswer == "l"):
                lowerBound = computerStoredAnswer + 1
            else:
                upperBound = computerStoredAnswer

playGuessingGame(1, 100)








