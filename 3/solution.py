highestPrimeFactor = 1
number = 600851475143
while number > 2:
    highestPrimeFactor = highestPrimeFactor + 1
    while number % highestPrimeFactor == 0:
        number = number/highestPrimeFactor

print(highestPrimeFactor)
