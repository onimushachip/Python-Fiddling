##Assignment for module 30

def hailstoneSequenceMax(firstTerm):
    maxValue = firstTerm
    oldNumber = firstTerm
    while oldNumber != 1:
        if (oldNumber % 2 == 0):
            newNumber = oldNumber // 2
        else:
            newNumber = 3 * oldNumber + 1
        oldNumber = newNumber
        if (newNumber > maxValue):
            maxValue = newNumber
    return(maxValue)

def longestHailstoneSequenceStartAndMax(lowStart, highStart):
    firstTermOfSequenceContainsMax = lowStart
    maxValueSoFar = 0
    for startValue in range (lowStart + 1, highStart + 1):
        maxValue = hailstoneSequenceMax(startValue)
        if (maxValue > maxValueSoFar):
            maxValueSoFar = maxValue
            firstTermOfSequenceContainsMax = startValue
    return firstTermOfSequenceContainsMax, maxValueSoFar

highestValue = 0
startingValue = 0
(startingValue, highestValue) = longestHailstoneSequenceStartAndMax(1, 50000)

print("highest value is: ", highestValue)
print("starting value of that sequence is: ", startingValue)