from random import randrange

##This function returns the result of rolling a fair dice
##This function returns an integer
def rollingDice():
    return randrange(1, 7)


timesOfGettingFour = 0

# ##Roll the dice 6000 times and record the times that get a four
# for i in range(6000):
#     if rollingDice() == 4:
#         timesOfGettingFour += 1
#
# print("There are ", timesOfGettingFour, " times of getting a four in 6000 rolls")


timesOfGettingTwo = 0
timesOfGettingSeven = 0

for i in range(36000):
    sumOfTwoDice = rollingDice() + rollingDice()
    if sumOfTwoDice == 2:
        timesOfGettingTwo = timesOfGettingTwo + 1
    if sumOfTwoDice == 7:
        timesOfGettingSeven = timesOfGettingSeven + 1

print("There are ", timesOfGettingTwo, " times of getting a two in 36000 rolls")
print("There are ", timesOfGettingSeven, " times of getting a seven in 36000 rolls")

