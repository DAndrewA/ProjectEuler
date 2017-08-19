sum = 0
currentNumber = 1
lastNumber = 0
while currentNumber < 4000000:
    if currentNumber % 2 == 0:
        sum += currentNumber

    nextNumber = currentNumber + lastNumber
    lastNumber = currentNumber
    currentNumber = nextNumber

print(sum)
