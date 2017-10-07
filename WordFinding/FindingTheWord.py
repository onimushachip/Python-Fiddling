from string import *

def analyzeWord(word):
    if 'the' == word[0:3]:
        return True
    else:
        return False

def readInFile():
    textFile = open("2246.txt", 'r')
    wordString = textFile.read()
    wordString.lower()
    wordList = wordString.split()
    textFile.close()
    return wordList

def checkNotDuplicate(word, wordList):
    for i in range(len(wordList)):
        if word == wordList[i]:
            return False
    return True

def removeDuplicate(wordList):
    newWordList = []
    for word in wordList:
        if not(word in newWordList):
            newWordList.append(word)
    return newWordList

def printWordList(wordList):
    for i in range(len(wordList)):
        print(wordList[i])

def checkText(wordList):
    wantedWord = []
    numberOfThe = 0
    for word in wordList:
        if word == 'the':
            numberOfThe += 1
        if analyzeWord(word):
            wantedWord.append(word)
    printWordList(removeDuplicate(wantedWord))
    print(numberOfThe)

checkText(readInFile())
