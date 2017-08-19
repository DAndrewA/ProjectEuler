# contains a list of all primes up to abitrarily picked cap (makes coding easier)
cap = 100000
primes = [p for p in range(2,cap) if 0 not in [p % n for n in range(2,int(p**0.5)+1)]]

def getNumDivisors(n):
    primeFactors = []
    newN = n
    currentP = 0
    numOfP = 0
    while newN > 1:
        if newN % primes[currentP] == 0:
            newN = newN / primes[currentP]
            numOfP += 1
        else:
            if numOfP != 0:
                primeFactors.append([primes[currentP],numOfP])
            numOfP = 0
            currentP += 1

    # calculate number of divisors
    numDivisors = 2
    for pf in primeFactors:
        numDivisors *= (pf[1]+1)

    return primeFactors,numDivisors

running = True
n = 1
# generates nth triangle numbers
while running:
    triangle = 0.5*n*(n+1)
    # find prime factors of triangle
    primeFactors,divisors = getNumDivisors(triangle)

    print(divisors)

    if divisors > 500:
        print(triangle)
        running = False
    n += 1
