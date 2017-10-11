testSequence = []

for i in range(0, 100):
    testSequence.append(i + 1)

def harmonicMean(myList):
    sum = 0.0
    for i in myList:
        sum += (1.0/i)
    return (len(myList)/sum)

print(harmonicMean(testSequence))

