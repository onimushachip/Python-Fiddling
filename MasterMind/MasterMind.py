import random
import string
# givenNumber = '12345'
# answer = '67890'
#
# print(givenNumber.index('1'))
# if givenNumber.index('1') == answer.index('1'):
#     print(True)


def generateQuest():
    quest = ''
    for i in range(0,5):
        number = random.randrange(0, 9)
        numberChar = str(number)
        while (numberChar in quest):
            number = random.randrange(0,9)
            numberChar = str(number)
        quest += numberChar
    return quest


def checkAnswerAndGivenNumber(quest):
    countingNumber = 0
    countingPosition = 0
    while (countingNumber < 5 or countingPosition < 5):
        countingNumber = 0
        countingPosition = 0
        answer = input("What do you think the number is?")
        for number in answer:
            if number in quest:
                countingNumber += 1
            if number in quest:
                if quest.index(number) == answer.index(number):
                    countingPosition += 1
        print("You guess", countingNumber, "number right")
        print("You guess", countingPosition, "position right")
        print("\n")
    print ("You got it right!")


quest = generateQuest()
print("I have a number in mind.")

checkAnswerAndGivenNumber(quest)

# I have a number in mind.
# What do you think the number is?14015
# You guess 4 number right
# You guess 1 position right
#
#
# What do you think the number is?11111
# You guess 5 number right
# You guess 0 position right
#
#
# What do you think the number is?14509
# You guess 3 number right
# You guess 0 position right
#
#
# What do you think the number is?14589
# You guess 3 number right
# You guess 0 position right
#
#
# What do you think the number is?14563
# You guess 2 number right
# You guess 0 position right
#
#
# What do you think the number is?14583
# You guess 3 number right
# You guess 0 position right
#
#
# What do you think the number is?14872
# You guess 3 number right
# You guess 2 position right
#
#
# What do you think the number is?14830
# You guess 3 number right
# You guess 1 position right
#
#
# What do you think the number is?14870
# You guess 4 number right
# You guess 2 position right
#
#
# What do you think the number is?15870
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?85170
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?18570
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?18507
# You guess 5 number right
# You guess 0 position right
#
#
# What do you think the number is?51870
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?51807
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?58170
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?58107
# You guess 5 number right
# You guess 0 position right
#
#
# What do you think the number is?51870
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?58170
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?71850
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?15870
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?57810
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?81057
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?78105
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?15870
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?17850
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?18750
# You guess 5 number right
# You guess 0 position right
#
#
# What do you think the number is?17805
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?71805
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?51807
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?75801
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?75810
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?71805
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?17805
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?17850
# You guess 5 number right
# You guess 1 position right
#
#
# What do you think the number is?71805
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?70815
# You guess 5 number right
# You guess 2 position right
#
#
# What do you think the number is?01857
# You guess 5 number right
# You guess 3 position right
#
#
# What do you think the number is?01875
# You guess 5 number right
# You guess 5 position right
#
#
# You got it right!




