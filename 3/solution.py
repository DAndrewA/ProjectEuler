primeFactors = []
number = 600851475143
while number > 2:
    for x in range(number):
        if x == 0:
            x = 1
        if number % x == 0:
            primeFactors.append(x)
            number = number / (x)
            break

print(primeFactors)
