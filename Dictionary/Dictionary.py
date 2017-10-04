import random

frenchDict = { 'one': 'un', 'two': 'deux',
	       'three':'trois', 'four':'quatre'}

def playGame():
    point = 0
    addressList = list(frenchDict.keys())
    random.shuffle(addressList)
    for address in addressList:
        print("what is your answer for", address, "?")
        answer = input()
        if answer == frenchDict[address]:
            print('You got it right')
            point += 1
        else:
            print('No. The correct answer is', frenchDict[address])
            print('Your answer is', answer)
    print("you got", point, "answer(s) right out of", len(frenchDict))

while (True):
    playGame()
    playAgain = input("Do you want to play again? Type no to quit.")
    if playAgain == "no":
        break

