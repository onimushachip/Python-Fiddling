from random import randrange

def tossingCoin():
    return randrange(1, 3)

##First part of the assignment
def playGame(tMoneyInput, hMoneyInput):
    tMoney = tMoneyInput
    hMoney = hMoneyInput
    timesCount = 0
    winner = "none"
    while (tMoney > 0 and hMoney > 0):
        if tossingCoin() == 1:
            tMoney = tMoney + 1
            hMoney = hMoney - 1
            timesCount += 1
            # print("On the toss number ", timesCount, " player T won, so H has $", hMoney, " and player T has ", tMoney)
        else:
            tMoney = tMoney - 1
            hMoney = hMoney + 1
            timesCount += 1
            # print("On the toss number ", timesCount, " player H won, so H has $", hMoney, " and player T has ", tMoney)
    if (tMoney > hMoney):
        winner = "t"
        return winner
    else:
        winner = "h"
        return winner

##print(playGame(10, 10)) ##Testing the playGame function with tMoney and hMoney are $10

##Second part of the assignment
def playMulitpleGames(tMoneyInput, hMoneyInput, playingTimes):
    tMoney = tMoneyInput
    hMoney = hMoneyInput
    probability = 0
    timesTWon = 0
    timesHWons = 0
    for i in range(playingTimes):
        if (playGame(tMoney, hMoney) == "t"):
            timesTWon = timesTWon + 1
        else:
            timesHWons = timesHWons + 1
    probability = timesHWons/playingTimes
    print(timesTWon)
    print(timesHWons)
    print("If player H starts with $", hMoneyInput, "and player T starts with $ ", tMoneyInput, " in ", playingTimes,
          "the probability that player H wins the game is ", probability)

playMulitpleGames(20, 1, 5000) ##Testing with 10000 games