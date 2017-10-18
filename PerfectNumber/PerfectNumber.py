##Program 3: Perfect Numbers

def isAProperDivisorOf(divisor, number):
    if (number%divisor == 0):
        return True
    else:
        return False

def sumOfTheProperDivisorsOf(number):
    sum = 0
    for i in range(1, number):
        if (isAProperDivisorOf(i, number) and i != number):
            # print(i)
            sum = sum + i
    # print(sum)
    return sum

def findPerfectNumbersIn(numnberToTest):
    for i in range(1, numnberToTest):
        if (sumOfTheProperDivisorsOf(i) == i):
            print(i)


# print(isAProperDivisorOf(3, 15))
# sumOfTheProperDivisorsOf(11)
findPerfectNumbersIn(100000)