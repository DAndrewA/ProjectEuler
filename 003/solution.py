'''
highestPrimeFactor = 0
number = 600851475143
while number > 2:
    highestPrimeFactor = highestPrimeFactor + 1
    while number % highestPrimeFactor == 0:
        number = number/highestPrimeFactor

print(highestPrimeFactor)
'''
# new solution
primeFactors = {2:0}
number = 600851475143
while number > 2:
    for i in range(3,int(number**0.5),2):
        if number % i == 0:
            if i in primeFactors:
                primeFactors[i] += 1
            else:
                primeFactors[i] = 1
            number = number/i
print(primeFactors) #read last (highest) value
